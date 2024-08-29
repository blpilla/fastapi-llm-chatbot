from fastapi import FastAPI
from pydantic import BaseModel
from transformers import LlamaForCausalLM, LlamaTokenizer
from langchain.agents import initialize_agent
from langchain.llms import HuggingFacePipeline

# Carregando o modelo LLaMA
model = LlamaForCausalLM.from_pretrained("path/to/llama/weights")
tokenizer = LlamaTokenizer.from_pretrained("path/to/llama/tokenizer")

# Criando o agente conversacional
llm = HuggingFacePipeline(model=model, tokenizer=tokenizer)
agent = initialize_agent([llm], agent="conversational-react-description", verbose=True)

app = FastAPI()

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(request: ChatRequest):
    response = get_chatbot_response(request.prompt)
    return {"response": response}

def get_chatbot_response(prompt):
    return agent.run(prompt)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
