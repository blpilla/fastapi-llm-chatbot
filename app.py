import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chat_models import ChatLlamaAPI
from langchain.schema import HumanMessage, AIMessage

# Set your LlamaAPI key
os.environ["LLAMA_API_KEY"] = "your-api-key-here"

# Initialize the ChatLlamaAPI model
chat_model = ChatLlamaAPI()

app = FastAPI()

class ChatInput(BaseModel):
    message: str

class ChatOutput(BaseModel):
    response: str

chat_history = []

@app.post("/chat", response_model=ChatOutput)
async def chat(chat_input: ChatInput):
    global chat_history
    
    # Add the user's message to the chat history
    chat_history.append(HumanMessage(content=chat_input.message))
    
    try:
        # Get the AI's response
        response = chat_model(chat_history)
        
        # Add the AI's response to the chat history
        chat_history.append(AIMessage(content=response.content))
        
        return ChatOutput(response=response.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the ChatLlamaAPI Chatbot!"}