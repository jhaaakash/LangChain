from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_template = ChatPromptTemplate(
    [
        ("system", "You are an helpful {domain} expert"),
        ("human", "Explain in simple terms, what is {topic}"),
        # SystemMessage(content="You are an helpful {domain} expert"),
        # HumanMessage(content="Explain in simple terms, what is {topic}"),
    ]
)

prompt = chat_template.invoke({"domain": "cricket", "topic": "dusra"})
print(prompt)
