import streamlit as st  # Import Streamlit
from pages.dashboard import dashboard_page
from pages.login import login_page

# Set page configuration
st.set_page_config(
    page_title="Business Dashboard",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add global CSS for a gradient background and universal styling
def add_global_styles():
    st.markdown(
        """
        <style>
            /* Global Gradient Background */
            body {
                background-color: rgba( #1E90FF, #87CEFA); /* Blue gradient */
                color: #000000; /* Text color */
                font-family: "Arial", sans-serif;
                margin: 0;
                padding: 0;
                overflow-x: hidden;
            }

            /* Headers Style */
            .main-header {
                text-align: center;
                font-size: 3rem;
                font-weight: bold;
                color: black;
                margin: 20px 0;
                text-shadow: 2px 2px #00509E;
            }

            .section-header {
                font-size: 1.8rem;
                color: black;
                margin-bottom: 10px;
                font-weight: bold;
            }

            /* Content Box Styling */
            .content-box {
                background-color: rgba(255, 255, 255, 0.9);
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }

            /* Sidebar Styling */
            .css-1aumxhk {
                background-color: rgba(255, 255, 255, 0.8);
                border-right: 2px solid #E5E5E5;
            }

            /* Footer Styling */
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background: #00509E;
                color: white;
                text-align: center;
                padding: 10px 0;
                font-size: 0.9rem;
            }

            /* Button Styling */
            .stButton>button {
                background-color: #0066CC !important;
                color: white !important;
                border-radius: 8px;
                padding: 10px 20px !important;
                border: none;
                font-weight: bold;
                font-size: 1rem;
                transition: transform 0.3s ease-in-out, background-color 0.3s;
            }
            .stButton>button:hover {
                background-color: #00509E !important;
                transform: scale(1.1);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

# Main function
def main():
    add_global_styles()  # Apply global styles

    # Initialize session state for managing authentication
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    # Render the appropriate page based on authentication state
    if not st.session_state.authenticated:
        # Login Page
        st.markdown("<div class='main-header'>Welcome to Business Dashboard</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='content-box'>Access insights, tools, and analytics to manage your business like a pro. Log in below to get started!</div>",
            unsafe_allow_html=True
        )

        # Login logic
        if login_page():
            st.session_state.authenticated = True
            st.experimental_rerun()
    else:
        # Dashboard Page
        st.markdown("<div class='main-header'>Dashboard</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='content-box'>Welcome back! Dive into analytics, manage operations, and explore insights to boost your business.</div>",
            unsafe_allow_html=True
        )

        # Render dashboard
        dashboard_page()

    # Footer
    st.markdown("<div class='footer'>Flaunch Internship | Level 2 project</div>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
