from pydantic import BaseModel, Field

class RecentYear(BaseModel):
    YearValue: str = Field(alias="코드")
    Year: str = Field(alias="코드명")

    class Config:
        from_attributes = True

class CurrentRecruitData(BaseModel):
    CurrentYear: str = Field(alias="mojib_yy")
    RecruitCategoryValue: str = Field(alias="mojib_gb")
    RecruitCategoryNM: str = Field(alias="mojib_gb_nm")

    class Config:
        from_attributes = True