from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=1.5, max_completion_tokens=200)
st.header("Welcome to paper Summarizer")
input = st.text_input("Enter your prompt")

if st.button("summarize"):
    result = model.invoke(input)
    st.write(result.content)
