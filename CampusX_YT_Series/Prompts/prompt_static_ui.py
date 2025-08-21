from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI()
st.header("Welcome to paper Summarizer")
input = st.text_input("Enter your prompt")

if st.button("summarize"):
    result = model.invoke(input)
    st.write(result.content)
