FitFeast.AI - Personalized Recipe Maker and Health Tips App
Welcome to FitFeast.AI! This app is your personal assistant for healthy eating, meal planning, and lifestyle guidance. FitFeast provides personalized recipes, sustainability insights, dietary goals, and daily routines to help you live a balanced lifestyle.

Features
Generate Recipe: Create recipes based on ingredients, cuisine, and dietary preferences.
Sustainability Score: Assess the environmental impact of selected dishes.
Dietary Goals: Get meal recommendations tailored to your dietary objectives.
Personalized Meal Plans: Design custom meal plans for your health goals.
Lifestyle Routine: Receive guidance on daily routines for a healthy lifestyle.
Multilingual Support: Recipes are available in multiple languages.
Prerequisites
Python 3.8+
Visual Studio Code (VSCode)
Conda Environment: Install Anaconda or Miniconda if not already installed.
Installation
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/fitfeast-ai.git
cd fitfeast-ai
Step 2: Create a Conda Environment
bash
Copy code
conda create --name fitfeast python=3.8
conda activate fitfeast
Step 3: Install Dependencies
bash
Copy code
pip install -r requirements.txt
Getting Your OpenAI API Key
To use OpenAI's models for generating recipes, sustainability insights, and more, you’ll need an OpenAI API key.

Sign Up: Go to OpenAI and create an account if you don't already have one.
Generate API Key:
Log in to your OpenAI account.
Go to the API Keys section in your OpenAI Dashboard.
Click Create new secret key and copy the generated API key.
Add API Key to the Project:
In the fitfeast-ai directory, create a file named .env.
Add your API key to the file in the following format:
bash
Copy code
OPENAI_API_KEY=your_openai_api_key_here
Running the App
Step 1: Load Environment Variables
Ensure your environment variables, including your OpenAI API key, are loaded by running:

bash
Copy code
source .env
Alternatively, you can set the key directly in the Python script.

Step 2: Launch the App
Run the Streamlit application:

bash
Copy code
streamlit run app.py
Step 3: Open in Browser
After the command runs, you’ll see a URL in the terminal. Open it in your browser to access the FitFeast.AI app.

Usage
Recipe Generation: Select ingredients, cuisine, and dietary preferences, then click Generate Recipe.
Sustainability Score: Input details about your dish to receive a sustainability score.
Dietary Goals: Choose your dietary objectives for customized recommendations.
Personalized Meal Plans: Enter your age, weight, and health goals to receive a tailored meal plan.
Lifestyle Routine: Get daily routine suggestions to complement your health goals.