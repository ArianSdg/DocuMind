from typing import Literal

from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field

from app.llm.factory import get_fast_llm
from app.prompts import CONDENSE_PROMPT, ROUTER_PROMPT


class RouteDecision(BaseModel):
    """Decide which system should handle a user question."""
    reasoning: str = Field(description="Provide a short explanation for the route decision")
    datasource: Literal["docs", "web", "direct"] = Field(
        description="Look up the sources 'docs/web/direct' for this decision"
    )


def build_router(llm=None):
    if llm is None:
        return ROUTER_PROMPT | get_fast_llm().with_structured_output(RouteDecision)

    return ROUTER_PROMPT | llm.with_structured_output(RouteDecision)


def build_condenser(llm=None):
    if llm is None:
        return CONDENSE_PROMPT | get_fast_llm() | StrOutputParser()

    return CONDENSE_PROMPT | llm | StrOutputParser()


def condense_question(question, history, condenser) -> str:
    if not history:
        return question

    return condenser.invoke({"question": question, "history": history})