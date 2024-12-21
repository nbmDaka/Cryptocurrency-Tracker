from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    CMC_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")

#
# settings = Settings()

try:
    settings = Settings()
except Exception as e:
    print(f"Error loading settings: {e}")
    raise