from functools import lru_cache

from langchain.agents import create_agent
from langchain.agents.middleware import ModelCallLimitMiddleware
from langchain_core.messages import ToolMessage

from app.agents.tools import get_agent_tools
from app.llm.factory import get_llm
from app.prompts import AGENT_SYSTEM


@lru_cache
def build_agent():
    return create_agent(
        model=get_llm(),
        tools=get_agent_tools(),
        system_prompt=AGENT_SYSTEM,
        middleware=[
            ModelCallLimitMiddleware(run_limit=6, exit_behavior="end")
        ]
    )


def run_agent(question, config=None) -> dict:
    agent = build_agent()
    out = dict()

    result = agent.invoke({"messages": [{"role": "human", "content": question}]}, config=config)

    out.update({
        "answer": result["messages"][-1].content,
        "tools_used": [m.name for m in result["messages"] if isinstance(m, ToolMessage)],
    })

    return out