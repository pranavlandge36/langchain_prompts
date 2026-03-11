from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()

st.header('Research Tool')

model=ChatNVIDIA(
    model="google/gemma-2-2b-it",
    api_key=os.getenv("NVIDIA_API_KEY"),
)

user_input=st.text_input('Enter your input')

if st.button('Summarize'):
    result=model.invoke(user_input)
    st.text(result.content)
 