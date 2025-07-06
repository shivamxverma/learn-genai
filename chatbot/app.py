from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Question:{question}"),
])

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write("You asked:", input_text)
    response = chain.invoke({"question": input_text})
    st.write("Response:", response)
