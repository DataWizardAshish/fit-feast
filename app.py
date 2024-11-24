import streamlit as st
from login_page import login_page
from fitfeast_home import fitfeast_home

# Routing logic
if "page" not in st.session_state:
    st.session_state["page"] = "login"

if st.session_state["page"] == "login":
    login_page()
elif st.session_state["page"] == "home":
    fitfeast_home()
