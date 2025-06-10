from datetime import date
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.memory import MemorySaver
from tools.tool_node import tool_node
from core.llm import kyra_llm

def should_continue(state: MessagesState):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END

def call_model(state: MessagesState):
    messages = state["messages"]
    today = date.today().strftime("%B %d, %Y")
    system_message = f"You are Kyra, a helpful and intelligent assistant. Today's date is {today}."

    response = kyra_llm.invoke({
        "system_message": system_message,
        "messages": messages
    })
    return {"messages": [response]}

workflow = StateGraph(MessagesState)
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)
workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", should_continue, ["tools", END])
workflow.add_edge("tools", "agent")

memory = MemorySaver()
graph_ = workflow.compile(checkpointer=memory)
