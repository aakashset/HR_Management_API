from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal

router = APIRouter(
    prefix="/designations",
    tags=["Designations"]
)


# Database Connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Designation
@router.post("/", response_model=schemas.DesignationResponse)
def create_designation(
    designation: schemas.DesignationCreate,
    db: Session = Depends(get_db)
):
    return crud.create_designation(db, designation)


# Get All Designations
@router.get("/", response_model=list[schemas.DesignationResponse])
def get_designations(
    db: Session = Depends(get_db)
):
    return crud.get_designations(db)


# Get Designation By ID
@router.get("/{designation_id}", response_model=schemas.DesignationResponse)
def get_designation(
    designation_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_designation(db, designation_id)


# Update Designation
@router.put("/{designation_id}", response_model=schemas.DesignationResponse)
def update_designation(
    designation_id: int,
    designation: schemas.DesignationCreate,
    db: Session = Depends(get_db)
):
    return crud.update_designation(
        db,
        designation_id,
        designation
    )


# Delete Designation
@router.delete("/{designation_id}")
def delete_designation(
    designation_id: int,
    db: Session = Depends(get_db)
):
    crud.delete_designation(db, designation_id)
    return {
        "message": "Designation Deleted Successfully"
    }