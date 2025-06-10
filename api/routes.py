# routes.py
from fastapi import APIRouter, HTTPException
from uuid import uuid4
from agents.kyra_agent import graph_
from models.schemas import ChatRequest, ChatResponse  

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(data: ChatRequest):
    try:
        thread_id = data.thread_id or str(uuid4())
        result = graph_.invoke(
            {"messages": [("human", data.message)]},
            config={"thread_id": thread_id}
        )
        ai_message = result["messages"][-1].content
        return {"response": ai_message, "thread_id": thread_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
