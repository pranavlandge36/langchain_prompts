from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI 
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

chat_history=[
    SystemMessage(content='you are jarvis from ironman , act like it'),
    HumanMessage(content='Hi')
]

while   True:
    user_input=input('You :')
    chat_history.append(HumanMessage(user_input))
    if user_input=='exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print('AI: ',result.content)
    print(chat_history)