import pyodbc
from fastapi import Depends, HTTPException, status
import asyncio
from app.core.database import get_db_connection_async

async def get_db_connection_dep() -> pyodbc.Connection:
    db_connection = None
    try:
        db_connection = await get_db_connection_async()

        yield db_connection
    except pyodbc.Error as ex:
        print(f"Database connection or operation error: {ex}")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error occurred"
        )
    finally:
        if db_connection:
            db_connection.close()