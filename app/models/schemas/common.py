from pydantic import BaseModel, Field 
from typing import Optional

class RecentYear(BaseModel):
    year: str

    class Config:
        from_attributes = True 


class CurrentRecruitData(BaseModel):
    current_year: str
    recruit_category_value: str
    recruit_category_name: str

    class Config:
        from_attributes = True
