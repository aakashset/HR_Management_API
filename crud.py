from sqlalchemy.orm import Session
import models
import schemas


# =========================
# DEPARTMENT
# =========================

# Create Department
def create_department(db: Session, department: schemas.DepartmentCreate):
    db_department = models.Department(
        department_name=department.department_name
    )

    db.add(db_department)
    db.commit()
    db.refresh(db_department)

    return db_department


# Get All Departments
def get_departments(db: Session):
    return db.query(models.Department).all()


# Get Department By ID
def get_department(db: Session, department_id: int):
    return (
        db.query(models.Department)
        .filter(models.Department.department_id == department_id)
        .first()
    )


# Update Department
def update_department(
    db: Session,
    department_id: int,
    department: schemas.DepartmentCreate
):
    db_department = get_department(db, department_id)

    if db_department:
        db_department.department_name = department.department_name

        db.commit()
        db.refresh(db_department)

    return db_department


# Delete Department
def delete_department(db: Session, department_id: int):
    db_department = get_department(db, department_id)

    if db_department:
        db.delete(db_department)
        db.commit()

    return db_department


# =========================
# DESIGNATION
# =========================

# Create Designation
def create_designation(
    db: Session,
    designation: schemas.DesignationCreate
):
    db_designation = models.Designation(
        designation_name=designation.designation_name
    )

    db.add(db_designation)
    db.commit()
    db.refresh(db_designation)

    return db_designation


# Get All Designations
def get_designations(db: Session):
    return db.query(models.Designation).all()


# Get Designation By ID
def get_designation(db: Session, designation_id: int):
    return (
        db.query(models.Designation)
        .filter(models.Designation.designation_id == designation_id)
        .first()
    )


# Update Designation
def update_designation(
    db: Session,
    designation_id: int,
    designation: schemas.DesignationCreate
):
    db_designation = get_designation(db, designation_id)

    if db_designation:
        db_designation.designation_name = designation.designation_name

        db.commit()
        db.refresh(db_designation)

    return db_designation


# Delete Designation
def delete_designation(db: Session, designation_id: int):
    db_designation = get_designation(db, designation_id)

    if db_designation:
        db.delete(db_designation)
        db.commit()

    return db_designation


# =========================
# CITY
# =========================

# Create City
def create_city(db: Session, city: schemas.CityCreate):
    db_city = models.City(
        city_name=city.city_name
    )

    db.add(db_city)
    db.commit()
    db.refresh(db_city)

    return db_city


# Get All Cities
def get_cities(db: Session):
    return db.query(models.City).all()


# Get City By ID
def get_city(db: Session, city_id: int):
    return (
        db.query(models.City)
        .filter(models.City.city_id == city_id)
        .first()
    )


# Update City
def update_city(
    db: Session,
    city_id: int,
    city: schemas.CityCreate
):
    db_city = get_city(db, city_id)

    if db_city:
        db_city.city_name = city.city_name

        db.commit()
        db.refresh(db_city)

    return db_city


# Delete City
def delete_city(db: Session, city_id: int):
    db_city = get_city(db, city_id)

    if db_city:
        db.delete(db_city)
        db.commit()

    return db_city


# =========================
# EMPLOYEE
# =========================

# Create Employee
def create_employee(
    db: Session,
    employee: schemas.EmployeeCreate
):
    db_employee = models.Employee(
        **employee.model_dump()
    )

    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)

    return db_employee


# =========================
# GET EMPLOYEES WITH PAGINATION
# =========================

def get_employees(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return (
        db.query(models.Employee)
        .offset(skip)
        .limit(limit)
        .all()
    )


# =========================
# GET EMPLOYEE BY ID
# =========================

def get_employee_by_id(db: Session, emp_id: int):
    return (
        db.query(models.Employee)
        .filter(models.Employee.emp_id == emp_id)
        .first()
    )


# =========================
# SEARCH EMPLOYEES
# =========================

def search_employees(
    db: Session,
    name: str = None,
    department_id: int = None,
    designation_id: int = None,
    city_id: int = None
):
    query = db.query(models.Employee)

    # Search by Employee Name
    if name:
        query = query.filter(
            models.Employee.emp_name.ilike(f"%{name}%")
        )

    # Search by Department
    if department_id is not None:
        query = query.filter(
            models.Employee.department_id == department_id
        )

    # Search by Designation
    if designation_id is not None:
        query = query.filter(
            models.Employee.designation_id == designation_id
        )

    # Search by City
    if city_id is not None:
        query = query.filter(
            models.Employee.city_id == city_id
        )

    return query.all()


# =========================
# UPDATE EMPLOYEE
# =========================

def update_employee(
    db: Session,
    emp_id: int,
    employee: schemas.EmployeeCreate
):
    db_employee = get_employee_by_id(db, emp_id)

    if db_employee:
        db_employee.emp_name = employee.emp_name
        db_employee.age = employee.age
        db_employee.salary = employee.salary
        db_employee.joining_date = employee.joining_date
        db_employee.department_id = employee.department_id
        db_employee.designation_id = employee.designation_id
        db_employee.city_id = employee.city_id

        db.commit()
        db.refresh(db_employee)

    return db_employee


# =========================
# DELETE EMPLOYEE
# =========================

def delete_employee(db: Session, emp_id: int):
    db_employee = get_employee_by_id(db, emp_id)

    if db_employee:
        db.delete(db_employee)
        db.commit()

    return db_employee