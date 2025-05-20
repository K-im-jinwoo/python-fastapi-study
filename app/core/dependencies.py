import pyodbc
from fastapi import Depends, HTTPException, status
import asyncio
from app.core.database import get_db_connection_async