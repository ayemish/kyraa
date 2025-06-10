# 🧠 Kyra — FastAPI LLM Assistant

Kyra is an intelligent assistant built with **FastAPI**, **LangGraph**, and **LangChain**, designed to handle conversational tasks like managing schedules, creating calendar events, and more — all through natural language.

---

## 🚀 Features

* 🧐 **LLM-powered** conversation flow using LangGraph + OpenAI
* 🔧 **Tool-based reasoning**: Kyra can call calendar tools via n8n webhooks
* 🗂️ Modular architecture: Clean separation of agents, tools, routes, and models
* 🌐 CORS enabled for frontend compatibility (e.g., React or Streamlit)

---

## 🏗️ Project Structure

```
KyraFastapi/
├── main.py                  # App entrypoint
├── api/
│   └── routes.py            # API routes
├── agents/
│   └── kyra_agent.py   # LangGraph agent and flow
├── core/
│   ├── config.py            # Future config setup
│   └── llm.py               # LLM bindings
├── models/
│   └── schemas.py           # Pydantic models for request/response
├── tools/
│   ├── tool_definitions.py  # Tool functions (create/update/delete events)
│   └── tool_node.py         # ToolNode object
├── .env                     # API keys (e.g. OpenAI)
└── requirements.txt         # Dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/kyra-fastapi.git
cd kyra-fastapi
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```


### 4. Add your `.env` file

Create a `.env` in the root directory:

```env
OPENAI_API_KEY=your-openai-api-key
```

---

## 🧪 Run the server

```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

---

## 📦 API Endpoint

### POST `/chat`

**Request Body:**

```json
{
  "message": "What's on my calendar today?",
  "thread_id": <thread_id>
}
```

**Response:**

```json
{
  "response": "You have 3 meetings today...",
  "thread_id": <thread_id>
}
```

---

## 🔮 Powered By

* [FastAPI](https://fastapi.tiangolo.com/)
* [LangChain](https://www.langchain.com/)
* [LangGraph](https://docs.langgraph.dev/)
* [OpenAI GPT-4o](https://platform.openai.com/)
* [n8n Webhooks](https://n8n.io/)

---

## 💡 Future Improvements

* Add Another Endpoint for generating threadid

---
