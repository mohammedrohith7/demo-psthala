from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "GenAI MLOps API"
    ENVIRONMENT: str = "development"
    
    # Azure OpenAI Settings
    AZURE_OPENAI_API_KEY: str = ""
    AZURE_OPENAI_ENDPOINT: str = ""
    AZURE_OPENAI_API_VERSION: str = "2023-12-01-preview"
    AZURE_OPENAI_DEPLOYMENT_NAME: str = "gpt-4"
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT: str = "text-embedding-ada-002"
    
    # Azure Search Settings (VectorDB)
    AZURE_SEARCH_ENDPOINT: str = ""
    AZURE_SEARCH_KEY: str = ""
    AZURE_SEARCH_INDEX_NAME: str = "knowledge-base"

    # External Data Sources (UAT/Prod parameterization)
    SERVICENOW_ENDPOINT: str = ""
    SERVICENOW_CREDENTIALS: str = ""
    
    KB_API_ENDPOINT: str = ""
    MIG_CONNECTION_STRING: str = ""
    D2OPS_API_KEY: str = ""

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
