from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# =========================
# DEPARTMENT
# =========================

class Department(Base):
    __tablename__ = "department"

    department_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    department_name = Column(
        String(100),
        nullable=False,
        unique=True
    )

    # Relationship with Employee
    employees = relationship(
        "Employee",
        back_populates="department"
    )


# =========================
# DESIGNATION
# =========================

class Designation(Base):
    __tablename__ = "designation"

    designation_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    designation_name = Column(
        String(100),
        nullable=False,
        unique=True
    )

    # Relationship with Employee
    employees = relationship(
        "Employee",
        back_populates="designation"
    )


# =========================
# CITY
# =========================

class City(Base):
    __tablename__ = "city"

    city_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    city_name = Column(
        String(100),
        nullable=False,
        unique=True
    )

    # Relationship with Employee
    employees = relationship(
        "Employee",
        back_populates="city"
    )


# =========================
# EMPLOYEE
# =========================

class Employee(Base):
    __tablename__ = "employee"

    # Primary Key
    emp_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    emp_name = Column(
        String(100),
        nullable=False
    )

    age = Column(
        Integer,
        nullable=False
    )

    salary = Column(
        Integer,
        nullable=False
    )

    joining_date = Column(
        Date,
        nullable=False
    )

    # =========================
    # FOREIGN KEYS
    # =========================

    department_id = Column(
        Integer,
        ForeignKey("department.department_id"),
        nullable=False
    )

    designation_id = Column(
        Integer,
        ForeignKey("designation.designation_id"),
        nullable=False
    )

    city_id = Column(
        Integer,
        ForeignKey("city.city_id"),
        nullable=False
    )

    # =========================
    # RELATIONSHIPS
    # =========================

    department = relationship(
        "Department",
        back_populates="employees"
    )

    designation = relationship(
        "Designation",
        back_populates="employees"
    )

    city = relationship(
        "City",
        back_populates="employees"
    )