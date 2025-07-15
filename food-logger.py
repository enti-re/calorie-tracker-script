import os
import re
import json
import datetime
from dotenv import load_dotenv
import google.generativeai as genai
from notion_client import Client

# --- 1. Load Environment Variables & Configure APIs ---
try:
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    NOTION_TOKEN = os.getenv("NOTION_TOKEN")
    NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

    if not all([GEMINI_API_KEY, NOTION_TOKEN, NOTION_DATABASE_ID]):
        raise ValueError("One or more environment variables are missing.")

    genai.configure(api_key=GEMINI_API_KEY)
    notion = Client(auth=NOTION_TOKEN)

except Exception as e:
    print(f"❌ ERROR: Initialization failed. {e}")
    exit()

def parse_to_average_int(value) -> int:
    """
    Parses a value that could be a number, a string, or a range (e.g., "500-600"),
    and returns an average integer.
    """
    if isinstance(value, int):
        return value
    
    # Convert value to string to handle all cases
    s_value = str(value)

    # If it's a range like "500-600", calculate the average
    if '-' in s_value:
        try:
            low, high = map(int, s_value.split('-'))
            return (low + high) // 2
        except ValueError:
            # Fallback if splitting fails
            pass

    # Find the first number in the string using regex
    numbers = re.findall(r'\d+', s_value)
    if numbers:
        return int(numbers[0])
    
    # Default to 0 if no number can be found
    return 0


def get_nutrition_from_gemini(food_input: str) -> dict:
    """Gets nutrition data from Gemini using JSON Mode."""
    print("🧠 Analyzing nutrition with Gemini...")

    model = genai.GenerativeModel(
        'gemini-1.5-flash',
        generation_config={"response_mime_type": "application/json"}
    )

    # Updated prompt to specifically ask for a single average number
    prompt = f"""
    Analyze the food description and provide a nutritional estimate.
    For each value (calories, protein, fiber), provide a single, average integer. Do not use ranges.
    Return only a JSON object with keys "calories", "protein", and "fiber".
    
    Food Description: "{food_input}"
    """

    try:
        response = model.generate_content(prompt)
        nutrition_data = json.loads(response.text)
        
        # ✅ Use the new parsing function to clean the data
        calories = parse_to_average_int(nutrition_data.get("calories", 0))
        protein = parse_to_average_int(nutrition_data.get("protein", 0))
        fiber = parse_to_average_int(nutrition_data.get("fiber", 0))

        print(f"📊 Estimated Nutrition: {calories} kcal, {protein}g protein, {fiber}g fiber")
        return {"calories": calories, "protein": protein, "fiber": fiber}

    except Exception as e:
        print(f"❌ ERROR: Failed to get or parse nutrition data: {e}")
        return None

def log_to_notion(food_input: str, nutrition_data: dict):
    """Logs the meal and its nutrition data to a Notion database."""
    print("📝 Sending data to Notion...")
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")

    try:
        notion.pages.create(
            parent={"database_id": NOTION_DATABASE_ID},
            properties={
                "Name": {"title": [{"text": {"content": food_input.title()}}]},
                "Calories": {"number": nutrition_data["calories"]},
                "Protein (g)": {"number": nutrition_data["protein"]},
                "Fiber (g)": {"number": nutrition_data["fiber"]},
                "Date": {"date": {"start": today_date}}
            }
        )
        print("✅ Successfully logged your meal to Notion!")
    except Exception as e:
        print(f"❌ ERROR: Failed to write to Notion. Check your Database ID and permissions.")
        print(f"   Details: {e}")

def main():
    """The main function that runs the food logger."""
    print("✅ Notion Food Logger Initialized")
    food_input = input("Enter the meal you ate: ")

    if not food_input:
        print("No input provided. Exiting.")
        return

    nutrition_data = get_nutrition_from_gemini(food_input)

    if nutrition_data:
        log_to_notion(food_input, nutrition_data)

if __name__ == "__main__":
    main()