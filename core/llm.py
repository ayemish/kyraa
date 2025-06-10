from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tools.tool_node import tools
from core.config import OPENAI_API_KEY, OPENAI_MODEL, DEFAULT_TEMPERATURE

model = ChatOpenAI(
    model=OPENAI_MODEL,
    api_key=OPENAI_API_KEY,
    temperature=DEFAULT_TEMPERATURE
).bind_tools(tools)

# Bind tools at this level
model_with_tools = model.bind_tools(tools)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "{system_message}"),
    MessagesPlaceholder("messages")
])

# Composable chain
kyra_llm = prompt_template | model_with_tools
