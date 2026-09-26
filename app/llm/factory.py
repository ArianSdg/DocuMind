from functools import lru_cache

from langchain.chat_models import init_chat_model

from app.core.config import get_settings

settings = get_settings()


def _get_provider_kwargs():
    if settings.llm_provider == "groq":
        return {
            "max_retries": 3
        }

    if settings.llm_provider == "ollama":
        return {
            "base_url": settings.ollama_base_url,
            "num_ctx": 32_768
        }

    return

@lru_cache
def get_llm():
    return init_chat_model(
        model=settings.llm_model,
        model_provider=settings.llm_provider,
        temperature=settings.llm_temperature,
        **_get_provider_kwargs()
    )

@lru_cache
def get_fast_llm():
    return init_chat_model(
        model=settings.fast_llm_model,
        model_provider=settings.llm_provider,
        temperature=0,
        **_get_provider_kwargs()
    )