from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
import os
load_dotenv()

# model=ChatNVIDIA(
#     model="google/gemma-2-2b-it",
#     api_key=os.getenv("NVIDIA_API_KEY"),
# )

model = ChatOpenAI(
    model="openai/gpt-4o-mini",  # or any model from OpenRouter
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

messages=[
    SystemMessage(content='you are jarvis from ironman , act like it'),
    HumanMessage(content='Hi')
]
result=model.invoke(messages)
print(result.content)
messages.append(AIMessage(content=result.content))
print(messages)