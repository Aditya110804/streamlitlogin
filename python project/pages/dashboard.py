import streamlit as st

# Prevent crash
if "username" not in st.session_state:
    st.session_state.username = ""
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("Welcome")

st.write(f"Hello, {st.session_state.username}!")

st.image("static/welcome.png", use_container_width=True)

if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.page = "login"
    st.session_state.username = ""
    st.rerun()
