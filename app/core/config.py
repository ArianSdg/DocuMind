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
    llm_provider: str = Field(default="openai")
    llm_model: str = Field(default="gpt-5.5")
    fast_llm_model: str = Field(default="") # Fill the default value
    llm_temperature: float = 0
    ollama_base_url: str = Field(default="") # Fill the default value
    database_url: str = Field(default="") # Fill the default value


@lru_cache
def get_settings() -> Settings:
    load_dotenv()
    return Settings()