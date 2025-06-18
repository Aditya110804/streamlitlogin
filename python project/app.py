import streamlit as st

# Initialize session
if "page" not in st.session_state:
    st.session_state.page = "login"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Navigation
if st.session_state.logged_in:
    from pages import dashboard
elif st.session_state.page == "signup":
    from pages import signup
else:
    from pages import login
