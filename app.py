import streamlit as st
from models.llama_utils import generate_itinerary

# Custom CSS for enhanced UI styling
def add_custom_css():
    st.markdown(
        """
        <style>
        /* Gradient background */
        body {
            background: linear-gradient(to bottom right, #0073e6, #ffffff);
            font-family: 'Arial', sans-serif;
            color: #000000;
        }
        
        /* Main container */
        .main {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 30px;
            margin: 20px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }
        
        /* Title styling */
        h1 {
            color: #0073e6;
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 3rem;
            text-align: center;
            margin-bottom: 20px;
        }
        
        /* Subheader styling */
        h2, h3, h4, p {
            color: #333333;
            font-family: 'Verdana', sans-serif;
        }

        /* Input fields styling */
        .stTextInput > div > div > input {
            background-color: #f0f8ff;
            border: 2px solid #0073e6;
            border-radius: 8px;
            padding: 10px;
            font-size: 18px;
            color: #333333;
        }
        
        /* Number input styling */
        .stNumberInput > div > div > input {
            background-color: #f0f8ff;
            border: 2px solid #0073e6;
            border-radius: 8px;
            padding: 10px;
            font-size: 18px;
            color: #333333;
        }

        /* Button styling */
        .stButton button {
            background-color: #0073e6;
            color: white;
            border-radius: 10px;
            font-size: 20px;
            font-weight: bold;
            padding: 10px 20px;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #005bb5;
        }

        /* Output message styling */
        .stAlert, .stMarkdown {
            color: #000000;
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Footer styling */
        footer {
            font-family: 'Courier New', monospace;
            color: #0073e6;
            text-align: center;
            margin-top: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Main function for the app
def main():
    # Add CSS for styling
    add_custom_css()
    
    # Add header and icons
    st.title("🌍 AI Travel Planner ✈️")
    
    # Add a subtle description
    st.subheader("Plan your perfect trip with AI-generated itineraries! ✨")
    st.write("Just provide your preferences, budget, and interests, and we'll take care of the rest! 🌟")

    # Create input sections with placeholders
    st.write("### Tell us more about your dream trip! 🏖️ 🗺️")
    preferences = st.text_input("Enter your travel preferences (e.g., adventure, relaxation, city tour):", placeholder="Type your preferences here...")
    budget = st.number_input("Enter your budget ($):", min_value=0, step=100)
    interests = st.text_input("Enter your interests (e.g., hiking, beaches, museums):", placeholder="Type your interests here...")
    
    # Generate itinerary button with conditional input validation
    if st.button("Generate Itinerary ✨"):
        if preferences and interests:
            itinerary = generate_itinerary(preferences, budget, interests)
            st.success("🎉 Here is your AI-generated itinerary:")
            st.write(itinerary)
        else:
            st.error("⚠️ Please fill out all fields to generate your itinerary!")

    # Add a footer with some travel-themed details
    st.write("")
    st.write("")
    st.markdown("""
    <footer>
        Powered by AI ✨ | Your ultimate travel planning assistant 🌐
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
