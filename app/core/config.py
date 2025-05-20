from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    #환경 변수 값을 자동으로 가져와 string타입으로 할당
    DATABASE_URL: str

    class Config:
        pass

settings = Settings()