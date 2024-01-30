from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_description: str = 'Приложения для переговорок, описание_1.'
    database_url: str

    class Config:
        env_file = '.env'

settings = Settings() 