import pyodbc 
from app.core.config import settings
import asyncio

#pyodbc.connect는 동기함수 -> asyncio로 비동기 실행
async def get_db_connection_async():
    loop = asyncio.get_event_loop()

    db_connection = await loop.run_in_executor(
        None,
        lambda: pyodbc.connect(settings.DATABASE_URL)
    )
    return db_connection