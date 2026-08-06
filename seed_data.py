from database import SessionLocal
import models

db = SessionLocal()

try:


    # DEPARTMENTS


    departments = [
        "Information Technology",
        "Human Resources",
        "Finance",
        "Sales",
        "Marketing"
    ]

    for department in departments:
        existing = (
            db.query(models.Department)
            .filter(models.Department.department_name == department)
            .first()
        )

        if not existing:
            db.add(
                models.Department(
                    department_name=department
                )
            )

    db.commit()


    # DESIGNATIONS


    designations = [
        "Software Engineer",
        "Data Engineer",
        "HR Executive",
        "Accountant",
        "Sales Executive",
        "Manager",
        "Business Analyst"
    ]

    for designation in designations:
        existing = (
            db.query(models.Designation)
            .filter(models.Designation.designation_name == designation)
            .first()
        )

        if not existing:
            db.add(
                models.Designation(
                    designation_name=designation
                )
            )

    db.commit()


    # CITIES


    cities = [
        "Chennai",
        "Bangalore",
        "Hyderabad",
        "Mumbai",
        "Coimbatore",
        "Delhi",
        "Kochi"
    ]

    for city in cities:
        existing = (
            db.query(models.City)
            .filter(models.City.city_name == city)
            .first()
        )

        if not existing:
            db.add(
                models.City(
                    city_name=city
                )
            )

    db.commit()

    print("===================================")
    print("Sample data inserted successfully!")
    print("Duplicate records were skipped.")
    print("===================================")

except Exception as e:
    db.rollback()
    print("Error:", e)

finally:
    db.close()