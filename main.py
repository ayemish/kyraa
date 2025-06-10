# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router  # Adjusted for new structure

app = FastAPI()

# Optional: CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your router
app.include_router(router)

# # main.py
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from langgraph_agent import graph_
# from uuid import uuid4
# from fastapi.middleware.cors import CORSMiddleware

# # Optional CORS (useful for frontend testing)
# origins = ["*"]

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class ChatRequest(BaseModel):
#     message: str
#     thread_id: str | None = None

# class ChatResponse(BaseModel):
#     response: str
#     thread_id: str

# @app.post("/chat", response_model=ChatResponse)
# async def chat(data: ChatRequest):
#     try:
#         thread_id = data.thread_id or str(uuid4())
#         result = graph_.invoke(
#             {"messages": [("human", data.message)]},
#             config={"thread_id": thread_id}
#         )
#         ai_message = result["messages"][-1].content
#         return {
#                 "response": ai_message,
#                 "thread_id": thread_id  # Return thread_id so client can reuse it
#             }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
