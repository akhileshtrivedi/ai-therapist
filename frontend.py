# Step1: Setup Streamlit
import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="SoulBalm", layout="wide")
st.title("🧠 Akhilesh – SoulBalm")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Step2: User is able to ask question
# Chat input
user_input = st.chat_input("What's on your mind today?")
if user_input:
    # Append user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # AI Agent exists here
    response = requests.post(BACKEND_URL, json={"message": user_input})
    fixed_dummy_response="I am here for you. You can share you problem with me and i am try to provide correct sollutions."
    #st.session_state.chat_history.append({"role": "assistant", "content": response.json()})
    #print(response)
    st.session_state.chat_history.append({"role": "assistant", "content": f'{response.json()["response"]} Provided By This Tool: [{response.json()["tool_called"]}]'})


# Step3: Show response from backend
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])