from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".envs/.env.local", env_file_encoding="utf-8", extra="ignore"
    )
    # App
    APP_NAME:str
    APP_DESCRIPTION:str
    APP_VERSION :str
    APP_URL_PREFIX:str

settings = Settings()