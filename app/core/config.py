from functools import lru_cache

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    app_name: str = Field(default="documind")
    environment: str = Field(default="development")
    llm_provider: str = Field(default="ollama")
    llm_model: str = Field(default="llama3.2")
    fast_llm_model: str = Field(default="") # Fill
    llm_temperature: float = 0
    ollama_base_url: str = Field(default="http://localhost:11434")
    database_url: str = Field(default="postgresql+psycopg://documind:documind@localhost:5432/documind")


@lru_cache
def get_settings() -> Settings:
    load_dotenv()
    return Settings()