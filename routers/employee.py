from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)



# DATABASE CONNECTION

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# CREATE EMPLOYEE

@router.post("/", response_model=schemas.EmployeeResponse)
def create_employee(
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    return crud.create_employee(db, employee)



# GET ALL EMPLOYEES

@router.get("/", response_model=list[schemas.EmployeeResponse])
def get_employees(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_employees(db, skip, limit)



# SEARCH EMPLOYEES

@router.get("/search/", response_model=list[schemas.EmployeeResponse])
def search_employee(
    name: Optional[str] = None,
    department_id: Optional[int] = None,
    designation_id: Optional[int] = None,
    city_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    return crud.search_employees(
        db,
        name,
        department_id,
        designation_id,
        city_id
    )



# GET EMPLOYEE BY ID

@router.get("/{emp_id}", response_model=schemas.EmployeeResponse)
def get_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    employee = crud.get_employee_by_id(db, emp_id)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee



# UPDATE EMPLOYEE

@router.put("/{emp_id}", response_model=schemas.EmployeeResponse)
def update_employee(
    emp_id: int,
    employee: schemas.EmployeeCreate,
    db: Session = Depends(get_db)
):
    updated_employee = crud.update_employee(
        db,
        emp_id,
        employee
    )

    if updated_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return updated_employee


# DELETE EMPLOYEE

@router.delete("/{emp_id}")
def delete_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    deleted_employee = crud.delete_employee(
        db,
        emp_id
    )

    if deleted_employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully."
    }