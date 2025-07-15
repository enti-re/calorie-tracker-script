AI Food Logger for Notion 🤖📝
A simple yet powerful Python script that uses the Google Gemini API to analyze your meals and automatically log them into a Notion database. Just describe what you ate, and let AI handle the rest.

Note: You should replace the placeholder image above with a GIF or screen recording of your script in action!

✨ Features
Natural Language Input: Describe your meal in plain English (e.g., "A bowl of dal, rice, and a side of yogurt").

AI-Powered Nutrition Analysis: Leverages the Gemini API to get an estimated breakdown of calories, protein, and fiber.

Automated Notion Logging: Automatically creates a new entry in your Notion database with the meal name, date, and nutritional info.

Simple & Extensible: Built with clean, commented Python, making it easy to understand and modify.

🛠️ Tech Stack
Language: Python 3

AI Model: Google Gemini API

Database: Notion API

Dependencies: python-dotenv, google-generativeai, notion-client

🚀 Setup and Installation Guide
Follow these steps to get the AI Food Logger running on your local machine.

Step 1: Prerequisites
Make sure you have Python 3.8 or newer installed on your system.

Step 2: Clone the Repository
Open your terminal and clone this repository:

git clone <your-repository-url>
cd <your-repository-name>

Step 3: Set Up Your Notion Database
This is the most important step. You need a specific database structure and a Notion API token.

Duplicate the Notion Template:

Go to this Notion template: Food Logger Template

Click "Get template" to duplicate it into your own Notion workspace.

This ensures your database has the correct properties: Name (Title), Calories (Number), Protein (g) (Number), Fiber (g) (Number), and Date (Date).

Create a Notion Integration:

Go to My Integrations.

Click the "+ New integration" button.

Give it a name (e.g., "Food Logger Bot") and associate it with your workspace.

On the next screen, copy your "Internal Integration Secret". This is your NOTION_TOKEN.

Get Your Database ID:

Open the Food Logger database you just duplicated in Notion.

Click the ... (three dots) icon in the top-right corner.

Click "Copy link to view".

The long string of characters (XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX) between your workspace name and the ? is your NOTION_DATABASE_ID.

Connect Your Integration to the Database:

Go back to your database page in Notion.

Click the ... icon again.

In the menu, click "+ Add connections" and search for the integration you created (e.g., "Food Logger Bot"). Select it to give it permission to access this database.

Step 4: Get Your Google Gemini API Key
Go to Google AI Studio.

Sign in with your Google account.

Click the "Get API key" button in the top left.

Click "Create API key in new project".

Copy the generated API key. This is your GEMINI_API_KEY.

Step 5: Configure Environment Variables
In the project folder, rename the .env.example file to .env.

Open the .env file and paste in the keys you just copied.

# .env file

GEMINI_API_KEY="PASTE_YOUR_GEMINI_API_KEY_HERE"
NOTION_TOKEN="PASTE_YOUR_NOTION_INTERNAL_INTEGRATION_SECRET_HERE"
NOTION_DATABASE_ID="PASTE_YOUR_NOTION_DATABASE_ID_HERE"

Step 6: Install Dependencies
Install all the required Python packages using the requirements.txt file.

pip install -r requirements.txt

▶️ How to Run the Script
You're all set! To run the food logger, simply execute the following command in your terminal:

python food_logger.py

The script will then prompt you to enter your meal description.

📂 Project Files
food_logger.py: The main Python script containing all the logic.

requirements.txt: A list of all the Python packages needed for the project.

.env: Your private file for storing API keys and secrets (you create this from .env.example).

💡 Future Ideas
Add support for image input (take a picture of your food).

Build a simple web interface using Flask or Streamlit.

Deploy it as a serverless function on AWS Lambda or Google Cloud Functions.

Create a Telegram or Discord bot interface.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.