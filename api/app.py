from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GEMINI_API_KEY']=os.getenv("GEMINI_API_KEY")


app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "A simple Langchain server using Google Gemini API",
)

add_routes(
    app,
    ChatGoogleGenerativeAI(model="gemini-2.5-pro"),
    path="/ai"
)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

prompt = ChatPromptTemplate.from_template("What is the capital of France?")

finalprompt = prompt | llm

add_routes(
    app,
    finalprompt,
    path="/prompt"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)