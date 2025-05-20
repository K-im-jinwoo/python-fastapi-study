from typing import Any, Dict, List, Optional, Type, TypeVar, Tuple
import pyodbc
import asyncio
from pydantic import BaseModel

# 결과를 매핑할 Pydantic 모델 타입(데이터 검증)을 위한 TypeVar
T = TypeVar("T", bound=BaseModel)

async def execute_procedure_query_async(
        db_connection: pyodbc.Connection, #FastAPI DI로 주입받은 DB 연결 객체
        procedure_name: str,
        parameters: Optional[Tuple] = None, #프로시저 매개변수
        result_model: Type[T] = BaseModel
) -> List[T]:
    loop = asyncio.get_event_loop()

    def sync_execute():
        cursor = db_connection.cursor()
        try:
            sql = f"EXEC {procedure_name}"
            if parameters:
                placeholders = ', '.join('?' for _ in parameters)
                sql = f"{sql} {placeholders}"
                cursor.execute(sql, parameters)
            else:
                cursor.execute(sql)
            
            columns = [column[0] for column in cursor.description]
            results = []
            rows = cursor.fetchall()

            for row in rows:
                row_data = dict(zip(columns, row))
                results.append(result_model(**row_data))
            return results
        except Exception as e:
            print(f"Error executing procedure {procedure_name}: {e}")
            db_connection.rollback()

            raise
        finally:
            cursor.close()

    return await loop.run_in_executor(None, sync_execute)

async def execute_procedure_query_single_async(
    db_connection: pyodbc.Connection,
    procedure_name: str,
    parameters: Optional[Tuple] = None,
    result_model: Type[T] = BaseModel
) -> Optional[T]: 
    
    results = await execute_procedure_query_async(db_connection, procedure_name, parameters, result_model)
    return results[0] if results else None