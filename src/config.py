from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL : str ='postgresql+asyncpg://admin:admin@localhost:5432/bookly_db'

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore'
    )

Config = Settings()