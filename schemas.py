from datetime import date
from pydantic import BaseModel, Field


# =========================
# DEPARTMENT
# =========================

class DepartmentBase(BaseModel):
    department_name: str = Field(..., min_length=2, max_length=100)


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentResponse(DepartmentBase):
    department_id: int

    class Config:
        from_attributes = True


# =========================
# DESIGNATION
# =========================

class DesignationBase(BaseModel):
    designation_name: str = Field(..., min_length=2, max_length=100)


class DesignationCreate(DesignationBase):
    pass


class DesignationResponse(DesignationBase):
    designation_id: int

    class Config:
        from_attributes = True


# =========================
# CITY
# =========================

class CityBase(BaseModel):
    city_name: str = Field(..., min_length=2, max_length=100)


class CityCreate(CityBase):
    pass


class CityResponse(CityBase):
    city_id: int

    class Config:
        from_attributes = True


# =========================
# EMPLOYEE
# =========================

class EmployeeBase(BaseModel):
    emp_name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    age: int = Field(
        ...,
        ge=18,
        le=60
    )

    salary: int = Field(
        ...,
        gt=0
    )

    joining_date: date

    department_id: int = Field(..., gt=0)
    designation_id: int = Field(..., gt=0)
    city_id: int = Field(..., gt=0)


# Used when creating/updating an employee
class EmployeeCreate(EmployeeBase):
    pass


# Used when returning employee data
class EmployeeResponse(EmployeeBase):
    emp_id: int

    department: DepartmentResponse
    designation: DesignationResponse
    city: CityResponse

    class Config:
        from_attributes = True