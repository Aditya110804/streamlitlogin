import streamlit as st
import json

def load_users():
    with open("data/users.json", "r") as f:
        return json.load(f)

st.title("Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    users = load_users()["users"]
    for user in users:
        if user["username"] == username and user["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()
            break
    else:
        st.error("Invalid credentials")

if st.button("Go to Signup"):
    st.session_state.page = "signup"
    st.rerun()
