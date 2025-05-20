from typing import List, Optional
import pyodbc # DB 연결 객체 타입 힌트 및 사용을 위해 필요
from fastapi import Depends # FastAPI DI 를 위해 필요

from app.models.domain.common import RecentYear, CurrentRecruitData
from app.repositories.interfaces import ICommonInfoRepository
# 공통 프로시저 호출 헬퍼 함수 임포트
from app.repositories.db_sp_utils import execute_procedure_query_async, execute_procedure_query_single_async
# DB 연결 객체 의존성 주입을 위한 헬퍼 함수 임포트
from app.core.dependencies import get_db_connection_dep


# ICommonInfoRepository 인터페이스를 실제로 구현하는 클래스
# FastAPI 의존성 주입(DI)을 통해 DB 연결 객체를 받아서 사용합니다.
class CommonInfoRepository():
    def __init__(self, db_connection: pyodbc.Connection = Depends(get_db_connection_dep)):
         self.db_connection = db_connection 


    # ICommonInfoRepository 인터페이스의 get_year_list 메서드
    # 년도 목록을 가져오는 프로시저를 호출
    async def get_year_list(self) -> List[RecentYear]:
        procedure_name = "uwindb1.입학행정_입시관리학부_기준정보관리_최근모집년도목록" 
        parameters = (p1,) 

        year_list_data = await execute_procedure_query_async(
            self.db_connection,
            procedure_name,
            parameters,
            RecentYear
        )

        return year_list_data # 매핑된 RecentYear 객체 목록 반환 (Service 로 전달)


    # ICommonInfoRepository 인터페이스의 get_current_recruit_info 메서
    # 현재 모집 정보를 가져오는 프로시저를 호출합니다.
    async def get_current_recruit_info(self) -> Optional[CurrentRecruitData]:
        procedure_name = "uwindb1.입학행정_입시관리학부_기준정보관리_현재모집년도모집구분" 
        parameters = (ibhag_gb,)

        recruit_info_data = await execute_procedure_query_single_async(
            self.db_connection, 
            procedure_name,
            parameters, 
            CurrentRecruitData 
        )

        return recruit_info_data # 매핑된 CurrentRecruitData 객체 또는 None 반환 (Service 로 전달)
