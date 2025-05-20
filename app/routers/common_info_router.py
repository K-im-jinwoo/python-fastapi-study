from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional

from app.services.interfaces import ICommonInfoService
from app.services.common_info_service import CommonInfoService # CommonInfoService 구현체 임포트
from app.models.schemas.common import RecentYear, CurrentRecruitData # schemas 모델 임포트


router = APIRouter(
    prefix="/common-info", # 이 라우터에 속한 모든 Endpoints 는 /common-info 로 시작
    tags=["Common Info"], # 자동 API 문서 (Swagger UI) 에 표시될 태그
    responses={ # 이 라우터의 모든 Endpoints 에 적용될 공통 응답 정의
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal Server Error"}
    },
)

CommonInfoServiceDep: ICommonInfoService = Depends(CommonInfoService)

# ✨ '/common-info/years' Endpoints 정의 (GET 요청) ✨
# 년도 목록을 반환하는 API
@router.get(
    "/years",
    response_model=List[RecentYear], 
    summary="최근 모집년도 목록" 
)
async def get_years_endpoint(
    p1: str,
    common_info_service: ICommonInfoService = CommonInfoServiceDep
):
    year_list_domain = await common_info_service.get_available_years(p1)
    
    return year_list_domain


# ✨ '/common-info/current-recruit' Endpoints 정의 (GET 요청) ✨
# 현재 모집 정보 (년도, 구분) 를 반환하는 API
@router.get(
    "/current-recruit",
    response_model=Optional[CurrentRecruitData],
    summary="현재모집년도모집구분"
)
async def get_current_recruit_endpoint(
    ibhag_gb: str,
    common_info_service: ICommonInfoService = CommonInfoServiceDep
):
     recruit_info_domain = await common_info_service.get_current_recruit_details(ibhag_gb)

     return recruit_info_domain



