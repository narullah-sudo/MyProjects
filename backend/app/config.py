from pydantic_settings import SettingsConfigDict, BaseSettings
import asyncpg
import psycopg
import psycopg_binary

class Settings(BaseSettings):
    DB_HOST: str
    DB_NAME: str
    DB_PORT: int
    DB_PASS: str
    DB_USER: str

    @property
    def sync_url(self):
        return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


    @property
    def async_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


    model_config = SettingsConfigDict(env_file = 'backend/.env')

settings = Settings()