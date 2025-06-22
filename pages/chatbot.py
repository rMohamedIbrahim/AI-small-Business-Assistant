import streamlit as st
from chatbot.business_assistant import BusinessAssistant  # Absolute import


def chatbot_page():
    st.header("AI Business Assistant")
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Initialize business assistant
    assistant = BusinessAssistant()
    
    # Context selector
    context_type = st.selectbox(
        "Select conversation context:",
        ["business_advice", "customer_support", "financial_guidance", "marketing_strategy"]
    )
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    user_input = st.chat_input("Ask your business question...")
    if user_input:
        # Display user message
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get and display assistant response
        response = assistant.get_response(user_input, context_type)
        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        

