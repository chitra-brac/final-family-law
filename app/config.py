"""
Application configuration settings
Loads environment variables and provides configuration object
"""

from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Application
    app_name: str = "Family Law Assistant"
    app_version: str = "1.0.0"
    debug: bool = False

    # OpenAI
    openai_api_key: str
    openai_model: str = "gpt-5.1-chat-latest"  # GPT-5.1 Chat for production

    # Supabase (optional - will use in-memory storage if not provided)
    supabase_url: str = ""
    supabase_key: str = ""

    # CORS
    cors_origins: list[str] = ["*"]  # In production, specify allowed origins

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance
    Using lru_cache ensures settings are loaded only once
    """
    return Settings()
