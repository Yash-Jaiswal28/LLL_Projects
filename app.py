from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"]="AIzaSyBT4Lqxo2V3zb34IN_1V32yGTmQR7AUItE"
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
google_api_key=os.getenv("LANGCHAIN_API_KEY")
print(google_api_key)

prompt =ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## Streamlit framework

st.title('Langchain Demo With Gemini API')
input_text=st.text_input("Search the topic u want")

##Gemini api

llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))