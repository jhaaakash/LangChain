from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")
result = model.invoke("Hi, What is the capital of US?")
print(result.content)
