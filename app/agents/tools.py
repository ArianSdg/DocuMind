import os

from langchain_tavily import TavilySearch

from app.core.config import get_settings


def web_search_enabled() -> bool:
    settings = get_settings()

    if not (settings.web_search_enabled and os.getenv("TAVILY_API_KEY")):
        return False

    return True


def get_web_search_tool() -> TavilySearch | None:
    if not web_search_enabled():
        return None

    return TavilySearch(max_results=3)


def get_agent_tools() -> list:
    result = get_web_search_tool()
    if result is None:
        return []

    return [result]
