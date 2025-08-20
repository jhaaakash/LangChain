from langchain_huggingface import HuggingFaceEmbeddings


# this will download the file at the local ans use that model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text = "Delhi is the capital of India"
vector = embedding.embed_query(text)
print(vector)
