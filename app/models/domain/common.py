from pydantic import BaseModel, Field

class RecentYear(BaseModel):
    year_value: str = Field(alias="코드")
    year: str = Field(alias="코드명")

    class Config:
        from_attributes = True

class CurrentRecruitData(BaseModel):
    current_year: str = Field(alias="mojib_yy")
    recruit_category_value: str = Field(alias="mojib_gb")
    recruit_category_name: str = Field(alias="mojib_gb_nm")

    class Config:
        from_attributes = True