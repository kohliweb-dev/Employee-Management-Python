from datetime import date
from pydantic import BaseModel , EmailStr, Field

class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    department: str
    salary: float = Field(gt=0)
    joining_date: date
    is_active: bool = True

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    department: str
    salary: float
    joining_date: date
    is_active: bool

    class Config:
        from_attributes = True


