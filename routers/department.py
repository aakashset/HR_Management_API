from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


# Database Connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Department
@router.post("/", response_model=schemas.DepartmentResponse)
def create_department(
    department: schemas.DepartmentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_department(db, department)


# Get All Departments
@router.get("/", response_model=list[schemas.DepartmentResponse])
def get_departments(
    db: Session = Depends(get_db)
):
    return crud.get_departments(db)


# Get Department By ID
@router.get("/{department_id}", response_model=schemas.DepartmentResponse)
def get_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    department = crud.get_department(db, department_id)

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return department


# Update Department
@router.put("/{department_id}", response_model=schemas.DepartmentResponse)
def update_department(
    department_id: int,
    department: schemas.DepartmentCreate,
    db: Session = Depends(get_db)
):
    updated_department = crud.update_department(
        db,
        department_id,
        department
    )

    if updated_department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return updated_department


# Delete Department
@router.delete("/{department_id}")
def delete_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    deleted_department = crud.delete_department(
        db,
        department_id
    )

    if deleted_department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return {
        "message": "Department deleted successfully"
    }