import streamlit as st
import sqlite3
from pathlib import Path

DB_FILE = "users.db"

def setup_local_database():
    """Initializes the SQLite database if it doesn't exist."""
    if not Path(DB_FILE).exists():
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    business_name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            """)
            conn.commit()

def save_user_to_local_db(business_name, email, password):
    """Saves user details to the SQLite database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO users (business_name, email, password)
                VALUES (?, ?, ?)
            """, (business_name, email, password))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False

# Function to add custom CSS


# Function to handle the login page
def login_page():
    st.title("🏪 Small Business Support Platform")
    
    setup_local_database()
# Apply the custom CSS

    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.header("Login")
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login"):
            with sqlite3.connect(DB_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id FROM users WHERE email = ? AND password = ?
                """, (email, password))
                user = cursor.fetchone()
                if user:
                    st.session_state['user_id'] = user[0]
                    st.session_state['authenticated'] = True
                    st.success("Login successful!")
                    return True  # Indicate successful login
                else:
                    st.error("Invalid credentials")
    
    with tab2:
        st.header("Register")
        business_name = st.text_input("Business Name")
        email = st.text_input("Email", key="register_email")
        password = st.text_input("Password", type="password", key="register_password")
        confirm_password = st.text_input("Confirm Password", type="password")
        
        if st.button("Register"):
            if password != confirm_password:
                st.error("Passwords don't match!")
            else:
                if save_user_to_local_db(business_name, email, password):
                    st.success("Registration successful! Please login.")
                    return False  # Return False to indicate registration done
                else:
                    st.error("Registration failed: Email already exists.")
    
    return False  # Return False by default if no action is completed
