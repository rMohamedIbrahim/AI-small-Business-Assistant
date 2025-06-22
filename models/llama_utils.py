import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain

# Directly set the Groq API key
GROQ_API_KEY = "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"  # Replace with your actual API key

def get_llama_model():
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not set. Please provide your API key in the script.")
    
    # Initialize the Groq client with the API key
    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model_name="llama-3.1-70b-versatile"
    )
    return llm

def generate_itinerary(preferences, budget, interests):
    try:
        # Get the LLM model
        llm = get_llama_model()
        
        # Define the prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a travel planner assistant. Generate a detailed travel itinerary based on the given preferences, budget, and interests."),
            ("human", "Preferences: {preferences}\nBudget: ${budget}\nInterests: {interests}\n\nPlease provide a day-by-day plan with activities and estimated costs.")
        ])
        
        # Create a chain for running the prompt with the LLM model
        chain = prompt | llm | StrOutputParser()
        
        # Run the chain with the input variables
        return chain.invoke({"preferences": preferences, "budget": budget, "interests": interests})
    except ValueError as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    # Test the function
    preferences = "Beach vacation, luxury hotels"
    budget = 5000
    interests = "Snorkeling, local cuisine"
    itinerary = generate_itinerary(preferences, budget, interests)
    print(itinerary)
