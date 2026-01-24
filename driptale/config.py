from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: str
    FIREBASE_CRED: str
    FIREBASE_STORAGE_BUCKET: str

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


settings = Settings()
