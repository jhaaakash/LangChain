from langchain_ollama.chat_models import ChatOllama
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model="gemma3:latest")
result = llm.invoke("what is the capital of Madhya Pradesh?")
print(result.content)
