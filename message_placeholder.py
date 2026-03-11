from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_core.messages import HumanMessage,AIMessage
from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
import os
load_dotenv()

chat_template=ChatPromptTemplate.from_messages([
    ('system','You are helpful, intelligent assistant, help your master and obey his commands'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history=[]

#load chat history
with open ('chat_history.txt') as f:
    chat_history.extend(f.readlines())

model = ChatOpenAI(
    model="openai/gpt-4o-mini",  # or any model from OpenRouter
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)
# query='And next?'

# prompt=chat_template.invoke({'chat_history':chat_history,'query':query})

# result=model.invoke((prompt))
# print(result.content)
# chat_history.append(HumanMessage(content=query))
# chat_history.append(AIMessage(content=result.content))

# print(chat_history)

while True:
    user_input=input('You :')
    chat_history.append(HumanMessage(user_input))
    if user_input=='exit':
        break
    prompt=chat_template.invoke({'chat_history':chat_history,'query':user_input})
    result =model.invoke((prompt))
    chat_history.append(AIMessage(result.content))
    print(result.content)