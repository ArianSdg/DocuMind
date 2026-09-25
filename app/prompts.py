from langchain_core.prompts import ChatPromptTemplate

SIMPLE_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are DocuMind, a concise assistant… at most 150 words… if unsure, say so"),
    ("human", "{question}"),
])