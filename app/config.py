"""
Application configuration settings
Loads environment variables and provides configuration object
"""

from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Application
    app_name: str = "Ain Bandhu"
    app_version: str = "1.0.0"
    debug: bool = False

    # OpenAI
    openai_api_key: str
    openai_model: str = "gpt-5.1-instant"  # GPT-5.1 Instant for production

    # Supabase (optional - will use in-memory storage if not provided)
    supabase_url: str = ""
    supabase_key: str = ""

    # CORS
    cors_origins: list[str] = ["*"]  # In production, specify allowed origins

    # Rate Limiting
    rate_limit_per_hour: int = 20  # messages per hour per IP
    rate_limit_per_session: int = 50  # messages per session

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
