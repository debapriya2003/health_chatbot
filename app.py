import streamlit as st
from auth import signup_user, login_user
from backend import generate_response, save_chat, get_chat_history

# Initialize session state variables
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = None
if "show_login" not in st.session_state:
    st.session_state.show_login = True  # Show login page by default


def show_login_page():
    """Display the login page."""
    st.title("Login to Health Chatbot")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        success, message = login_user(username, password)
        if success:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.show_login = False  # Hide login page
            st.experimental_set_query_params(page="chat")  # Optional, for bookmarking
            st.success(message)
        else:
            st.error(message)


def show_signup_page():
    """Display the signup page."""
    st.title("Sign Up for Health Chatbot")
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")
    if st.button("Sign Up"):
        success, message = signup_user(username, password)
        if success:
            st.success(message)
            st.info("Please log in with your new credentials.")
            st.session_state.show_login = True  # Redirect to login page
        else:
            st.error(message)


def show_chat_page():
    """Display the chatbot interface."""
    st.title(f"Welcome, {st.session_state.username}!")
    if st.sidebar.button("Logout"):
        logout()

    user_input = st.text_input("Ask me anything about your health:")
    if st.button("Submit"):
        if user_input:
            response = generate_response(user_input)
            st.text_area("Chatbot Response:", value=response, height=150)
            save_chat(st.session_state.username, user_input, response)
        else:
            st.error("Please enter a question!")

    if st.button("Show Chat History"):
        history = get_chat_history(st.session_state.username)
        if history:
            for chat in history:
                st.write(f"**User:** {chat['user_message']}")
                st.write(f"**Bot:** {chat['bot_response']}")
        else:
            st.write("No chat history found.")


def logout():
    """Log out the user."""
    st.session_state.authenticated = False
    st.session_state.username = None
    st.session_state.show_login = True  # Redirect to login page


# Main app logic
if not st.session_state.authenticated:
    if st.session_state.show_login:
        show_login_page()
    else:
        show_signup_page()
else:
    show_chat_page()
