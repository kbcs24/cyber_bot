import streamlit as st
from openai import openAI

# Initialize OpenAI client
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set app title
st.title("SOC-Support-Desk")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to get OpenAI response
def get_response(prompt, history):
    messages = [{"role": "system", "content": "You are a cybersecurity expert specializing in ethical hacking, penetration testing, incident management, and general cybersecurity solutions. Provide expert-level responses to any cybersecurity-related queries."}] + history + [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response["choices"][0]["message"]["content"]

# User input
user_input = st.chat_input("Type your cybersecurity question...")
if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get assistant response
    response = get_response(user_input, st.session_state.messages)
    
    # Append assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
