import streamlit as st
from firebase_config import auth, db

# Ensure session state is initialized
if "page" not in st.session_state:
    st.session_state["page"] = "login"  # Default page is login

def login_page():
    st.title("FitFeast Login")
    # Provide a globally unique key for the selectbox
    option = st.sidebar.selectbox("Choose Action", ["Login", "Sign Up"], key="unique_login_signup_option")

    if option == "Sign Up":
        email = st.text_input("Enter your email", key="unique_signup_email")
        name = st.text_input("Enter your name", key="unique_signup_name")
        password = st.text_input("Enter your password", type="password", key="unique_signup_password")
        if st.button("Sign Up", key="unique_signup_button"):
            try:
                user = auth.create_user_with_email_and_password(email, password)
                db.child("users").push({"name": name, "email": email})
                st.success("Account created successfully! Please log in.")
            except Exception as e:
                st.error(f"Error: {e}")
    elif option == "Login":
        email = st.text_input("Enter your email", key="unique_login_email")
        password = st.text_input("Enter your password", type="password", key="unique_login_password")
        if st.button("Log In", key="unique_login_button"):
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.success(f"Welcome back, {email}!")
                st.session_state["user"] = user
                st.session_state["page"] = "home"  # Navigate to home page
                st.rerun()
                
            except Exception as e:
                st.error(f"Error: {e}")

# Render pages based on session state
if st.session_state["page"] == "login":
    login_page()
elif st.session_state["page"] == "home":
    home_page()
