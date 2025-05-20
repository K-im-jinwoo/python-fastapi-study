from typing import List, Optional
from fastapi import Depends # FastAPI DI 를 위해 필요

from app.models.domain.common import RecentYear, CurrentRecruitData
from app.services.interfaces import ICommonInfoService
from app.repositories.interfaces import ICommonInfoRepository
from app.repositories.common_info_repository import CommonInfoRepository


class CommonInfoService():

    def __init__(self, common_info_repo: ICommonInfoRepository = Depends(CommonInfoRepository)):
        self.common_info_repo = common_info_repo 

    async def get_available_years(self, p1:str) -> List[RecentYear]:
        year_list_data = await self.common_info_repo.get_year_list()

        return year_list_data #

    async def get_current_recruit_details(self, ibhag_gb:str) -> Optional[CurrentRecruitData]:
        recruit_info_data = await self.common_info_repo.get_current_recruit_info()

        return recruit_info_data 