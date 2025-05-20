# Repository 계층의 인터페이스 정의 (Protocol 사용)
from typing import List, Optional, Protocol
from app.models.domain.common import RecentYear, CurrentRecruitData

class ICommonInfoRepository(Protocol): # Protocol 사용
    # ✨ '년도 목록 가져오기' 기능을 약속하는 메서드 정의! ✨
    # 이 메서드는 비동기 함수이며, RecentYear 객체들의 리스트를 반환해야 합니다.
    async def get_year_list(self, p1:str) -> List[RecentYear]:
        """년도 목록을 가져오는 프로시저를 호출하여 결과를 반환합니다."""
        ... # 인터페이스에서는 구현 코드를 작성하지 않습니다.

    # ✨ '현재 모집 정보 가져오기' 기능을 약속하는 메서드 정의! ✨
    # 이 메서드는 비동기 함수이며, CurrentRecruitData 객체 또는 None 을 반환해야 합니다.
    async def get_current_recruit_info(self, ibhag_gb:str) -> Optional[CurrentRecruitData]:
        """현재 모집 년도 및 모집 구분을 가져오는 프로시저를 호출하여 결과를 반환합니다."""
        ... # 인터페이스에서는 구현 코드를 작성하지 않습니다.
