from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Bhopal is the capital of M.P.",
    "Patna is the capital of Bihar",
]
vector_result = embedding.embed_documents(documents)

print(vector_result)
