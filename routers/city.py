from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal


router = APIRouter(
    prefix="/cities",
    tags=["Cities"]
)


# =========================
# DATABASE CONNECTION
# =========================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# CREATE CITY
# =========================

@router.post("/", response_model=schemas.CityResponse)
def create_city(
    city: schemas.CityCreate,
    db: Session = Depends(get_db)
):
    return crud.create_city(db, city)


# =========================
# GET ALL CITIES
# =========================

@router.get("/", response_model=list[schemas.CityResponse])
def get_cities(
    db: Session = Depends(get_db)
):
    return crud.get_cities(db)


# =========================
# GET CITY BY ID
# =========================

@router.get("/{city_id}", response_model=schemas.CityResponse)
def get_city(
    city_id: int,
    db: Session = Depends(get_db)
):
    city = crud.get_city(db, city_id)

    if city is None:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )

    return city


# =========================
# UPDATE CITY
# =========================

@router.put("/{city_id}", response_model=schemas.CityResponse)
def update_city(
    city_id: int,
    city: schemas.CityCreate,
    db: Session = Depends(get_db)
):
    updated_city = crud.update_city(
        db,
        city_id,
        city
    )

    if updated_city is None:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )

    return updated_city


# =========================
# DELETE CITY
# =========================

@router.delete("/{city_id}")
def delete_city(
    city_id: int,
    db: Session = Depends(get_db)
):
    deleted_city = crud.delete_city(
        db,
        city_id
    )

    if deleted_city is None:
        raise HTTPException(
            status_code=404,
            detail="City not found"
        )

    return {
        "message": "City deleted successfully"
    }