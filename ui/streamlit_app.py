import streamlit as st
import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from models.llama_utils import generate_itinerary

def main():
    st.title("AI Travel Planner")
    
    preferences = st.text_input("Enter your travel preferences:")
    budget = st.number_input("Enter your budget:", min_value=0, step=100)
    interests = st.text_input("Enter your interests:")
    
    if st.button("Generate Itinerary"):
        itinerary = generate_itinerary(preferences, budget, interests)
        st.write(itinerary)

if __name__ == "__main__":
    main()