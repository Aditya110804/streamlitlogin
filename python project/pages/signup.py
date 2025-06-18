import streamlit as st
import json
import os

def load_users():
    if os.path.exists("data/users.json"):
        with open("data/users.json", "r") as f:
            return json.load(f)
    return {"users": []}

def save_users(data):
    with open("data/users.json", "w") as f:
        json.dump(data, f, indent=4)

st.title("Signup Page")

new_username = st.text_input("New Username")
new_password = st.text_input("New Password", type="password")

if st.button("Create Account"):
    users = load_users()
    if not new_username or not new_password:
        st.warning("Enter all fields")
    elif any(u["username"] == new_username for u in users["users"]):
        st.warning("Username already exists")
    else:
        users["users"].append({"username": new_username, "password": new_password})
        save_users(users)
        st.success("Account created! Go to login.")
        st.session_state.page = "login"
        st.rerun()

if st.button("Go to Login"):
    st.session_state.page = "login"
    st.rerun()
