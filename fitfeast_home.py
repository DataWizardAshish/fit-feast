import openai
import streamlit as st
import requests
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image
import os

load_dotenv()

def fitfeast_home():
    # Set OpenAI API key
    openai.api_key = os.getenv('OPENAI_API_KEY')
    # Add Logout button in the sidebar
    if st.sidebar.button("Log Out", key="unique_logout_button"):
        st.session_state["page"] = "login"  # Navigate back to login page
        st.session_state.pop("user", None)  # Clear user session
        st.rerun()

    # Display logged-in user's email at the top
    if "user" in st.session_state and st.session_state["user"]:
        user_email = st.session_state["user"].get("email", "User")  # Fetch email from session
        st.write(f"👋 **Welcome, {user_email}!**")
    else:
        st.warning("No user session found. Please log in again.")
        st.session_state["page"] = "login"
        st.rerun()

    # Initialize session state for the welcome message
    st.sidebar.info(
        "👋 Welcome to FitFeast! Here’s how to get started:\n\n"
        "1. **Generate Recipe**: Select ingredients, cuisine, and dietary preferences to create a personalized recipe.\n"
        "2. **Sustainability Score**: Estimate the environmental impact of your chosen dish.\n"
        "3. **Dietary Goals**: Get recommendations tailored to your dietary objectives.\n"
        "4. **Personalized Plans**: Create meal plans based on your health goals and preferences.\n\n"
        "5. **Lifestyle Routine**: Check your Daily Routine to Stay Fit.\n\n"
        "Happy cooking! 🍽️"
    )
    
    st.title("FitFeast.AI")

    # Tabs for different features
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Generate Recipe", 
        "Sustainability Score", 
        "Dietary Goals", 
        "Personalized MealPlans", 
        "Lifestyle Routine", 
        "About Us"
    ])

    # Tab 1: Recipe Generation
    with tab1:
        language_choice = st.selectbox("Choose Language", ["English", "Hindi", "French", "Spanish"])
        food_type = st.selectbox("Choose Veg or Non-Veg", ["Veg", "Non-Veg"])
        cuisine_choice = st.selectbox("Select Cuisine", ["Indian", "Chinese", "Global", "Other"])

        if cuisine_choice == "Other":
            cuisine = st.text_input("Enter your cuisine")
        else:
            cuisine = cuisine_choice

        if cuisine == "Indian":
            dish = st.selectbox("Select Dish", ["Dal", "Rajma", "Idli", "Other"])
            if dish == "Other":
                dish = st.text_input("Enter your dish")
        else:
            dish = "Standard Dish"

        dietary_restrictions = st.multiselect("Dietary Restrictions", ["Vegan", "Gluten-Free", "Nut-Free"])
        people = st.number_input("Number of People", min_value=1, step=1)

        if st.button("Generate Recipe"):
            recipe_prompt = f"Create a {food_type} {cuisine} {dish} recipe for {people} people. Dietary restrictions: {', '.join(dietary_restrictions)}. Provide the recipe in {language_choice}. Include estimated preparation and cooking time.As a separate heading, suggest health benefits, nutritional value, and when not to eat this recipe.Provide responses with clear sections for each requested feature."
            recipe_response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=recipe_prompt,
                max_tokens=3000
            )
            recipe = recipe_response.choices[0].text.strip()
            st.subheader(f"Recipe in {language_choice}")
            st.write(recipe)

            # Generate TTS using OpenAI's API
            speech_response = openai.audio.speech.create(
                model="tts-1",
                voice="nova",  # Choose different voices if needed
                input=recipe
            )
            
            # Play audio using Streamlit
            audio_content = speech_response.content
            st.audio(audio_content, format="audio/mpeg")


    # Tab 2: Sustainability Score
    with tab2:
        st.subheader("Sustainability Score")
        sustainability_food_type = st.selectbox("Choose Veg, Non-Veg, or Vegan", ["Veg", "Non-Veg", "Vegan"])
        sustainability_cuisine = st.selectbox("Select Cuisine", ["Indian", "Chinese", "Global", "Other"], key="sustainability_cuisine")
        if sustainability_cuisine == "Other":
            sustainability_cuisine = st.text_input("Enter your cuisine", "")

        if st.button("Calculate Sustainability Score"):
            sustainability_prompt = f"Evaluate the sustainability score for a {sustainability_food_type} dish in {sustainability_cuisine}. Provide insights on ingredient choices, environmental impact, and suggestions for making the dish more sustainable. Provide a detailed breakdown of the carbon footprint of typical ingredients used. Suggest alternatives for high-impact ingredients and provide tips to make the dish more environmentally friendly.Provide responses with clear sections for each requested feature."
            sustainability_response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=sustainability_prompt,
                max_tokens=3000
            )
            sustainability_score = sustainability_response.choices[0].text.strip()
            st.subheader("Sustainability Insights")
            st.write(sustainability_score)

    # Tab 3: Dietary Goals
    with tab3:
        st.subheader("Dietary Goals")
        dietary_goal = st.selectbox("Select your dietary goal", ["Weight Loss", "Weight Gain", "Muscle Gain", "Balanced Diet"], key="dietary_goal")
        diet_preference = st.selectbox("Choose Veg, Non-Veg, or Vegan", ["Veg", "Non-Veg", "Vegan"], key="dietary_preference")

        if st.button("Get Dietary Goals"):
            dietary_goal_prompt = f"Provide dietary recommendations for {dietary_goal} with {diet_preference} options. Include daily caloric intake and macronutrient breakdown for effective planning. Suggest complementary exercises or lifestyle adjustments tailored to the goal for a holistic approach.Provide responses with clear sections for each requested feature."
            dietary_goal_response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=dietary_goal_prompt,
                max_tokens=3000
            )
            dietary_goals = dietary_goal_response.choices[0].text.strip()
            st.subheader("Dietary Recommendations")
            st.write(dietary_goals)

    # Tab 4: Personalized Plans
    with tab4:
        st.header("Personalized Meal Plan")
        age = st.number_input("Enter your age", min_value=0, max_value=120)
        gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])
        height = st.number_input("Enter your height (cm)", min_value=50, max_value=250)
        weight = st.number_input("Enter your weight (kg)", min_value=30, max_value=300)
        activity_level = st.selectbox("Select Activity Level", ["Sedentary", "Moderately Active", "Very Active"])
        foods_to_avoid = st.text_input("Foods to Avoid (comma-separated)")
        health_goals = st.selectbox("Select Health Goals", ["Lose Weight", "Gain Muscle", "Maintain Weight"])
        cooking_time = st.number_input("Time to Prepare (minutes)", min_value=5, max_value=180)
        budget = st.number_input("Total Cost (in $)", min_value=1, max_value=500)

        if st.button("Generate Personalized Meal Plan"):
            prompt = f"Create a personalized meal plan for a {age}-year-old {gender} who is {height} cm tall, weighs {weight} kg, and is {activity_level.lower()}. Their health goal is to {health_goals.lower()}. They want to avoid: {foods_to_avoid}. Include meals that can be prepared in under {cooking_time} minutes and keep the total cost under ${budget}.Provide responses with clear sections for each requested feature."
            meal_plan_response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=prompt,
                max_tokens=3000
            )
            meal_plan = meal_plan_response.choices[0].text.strip()
            st.subheader("Your Personalized Meal Plan")
            st.write(meal_plan)

    # Tab 5: Lifestyle Routine
    with tab5:
        st.header("Personalized Lifestyle Routine")
        # Inputs for lifestyle
        season = st.selectbox("Select Season", ["Spring", "Summer", "Fall", "Winter"])
        country = st.text_input("Enter your Country")
        age = st.number_input("Enter your Age", min_value=1, max_value=120)
        gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
        pregnancy_status = st.selectbox("Are you pregnant?", ["Yes", "No"])
        job_type = st.text_input("What is your Job?")
        job_timing = st.selectbox("Job Timing", ["Day Shift", "Night Shift", "Flexible"])
        workout_time = st.number_input("Available Workout Time (minutes)", min_value=0, max_value=180)

        if st.button("Generate Full-Day Routine"):
            routine_prompt = f"""
Create a full-day routine for a {age}-year-old from {country} during {season}. 
Pregnancy Status: {pregnancy_status}. 
Job: {job_type} ({job_timing}). 
Available workout time: {workout_time} minutes. 

Include:
- Stress management tips, including mindfulness or stress-relief exercises tailored to job timing and activity level.
- Suggestions for balancing family and social life to promote mental health.
- Weather-specific adjustments, such as indoor exercises for rainy days or hydration tips for hot weather.
- Sleep optimization advice based on routine and job timing.

Provide responses with clear sections for each requested feature.
"""
            routine_response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=routine_prompt,
                max_tokens=3000
            )
            full_day_routine = routine_response.choices[0].text.strip()
            st.subheader("Your Personalized Full-Day Routine")
            st.write(full_day_routine)

    # Tab 6: About Us
    with tab6:
        st.header("About FitFeast")
        st.write("👋 Welcome to FitFeast! We believe that healthy cooking should be enjoyable and accessible for everyone.")
        st.write("🍽️ Our app helps you create personalized meal plans, generate delicious recipes, and evaluate the sustainability of your food choices.")
        st.write("🌱 Whether you’re aiming to boost your energy, lose weight, or simply explore new cuisines, FitFeast is here for you!")
        st.image("https://example.com/healthy_food_image.jpg", caption='Healthy and Delicious Meals')
