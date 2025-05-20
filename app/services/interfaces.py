from typing import List, Optional, Protocol
# (Service 는 domain 모델을 다룹니다)
from app.models.domain.common import RecentYear, CurrentRecruitData
# Service 는 Repository '인터페이스'에 의존
from app.repositories.interfaces import ICommonInfoRepository

class ICommonInfoService(Protocol): # Protocol 사용
    async def get_available_years(self, p1:str) -> List[RecentYear]:
         """사용 가능한 년도 목록을 가져오는 비즈니스 로직을 수행합니다."""
         ... # 인터페이스에서는 구현 코드를 작성하지 않습니다.

    async def get_current_recruit_details(self, ibhag_gb:str) -> Optional[CurrentRecruitData]:
         """현재 모집 정보를 가져오는 비즈니스 로직을 수행합니다."""
         ... # 인터페이스에서는 구현 코드를 작성하지 않습니다.
