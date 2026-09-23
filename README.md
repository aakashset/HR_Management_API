# 🏢 HR Management System

A full-stack **Human Resource Management System** built with **FastAPI, SQLAlchemy, MySQL, and Streamlit**.

This project provides a RESTful API for managing employee information along with related **departments, designations, and cities**. A Streamlit-based frontend is included to provide a simple interactive interface for managing and viewing HR data.

---

## 📌 Project Overview

The HR Management System is designed to simplify basic HR data management through a structured backend API and an interactive web interface.

The application follows a modular architecture:

```text
                    ┌──────────────────────┐
                    │    Streamlit UI      │
                    │   Interactive Web UI  │
                    └──────────┬───────────┘
                               │
                               │ HTTP Requests
                               ▼
                    ┌──────────────────────┐
                    │     FastAPI API      │
                    │    REST Endpoints    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      CRUD Layer      │
                    │  Database Operations │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ SQLAlchemy ORM       │
                    │       Models         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       MySQL          │
                    │    hr_management     │
                    └──────────────────────┘
```

The FastAPI application registers separate routers for employees, departments, designations, and cities.

---

## ✨ Features

### 👨‍💼 Employee Management

* Create employees
* View all employees
* View employee by ID
* Update employee information
* Delete employees
* Search employees
* Filter employees by:

  * Name
  * Department
  * Designation
  * City
* Pagination using `skip` and `limit`

Employee records contain information such as employee name, age, salary, joining date, department, designation, and city.

---

### 🏢 Department Management

* Create department
* View all departments
* View department by ID
* Update department
* Delete department

Departments have a relationship with employees through SQLAlchemy ORM.

---

### 💼 Designation Management

* Create designation
* View all designations
* View designation by ID
* Update designation
* Delete designation

Designations are connected to employee records through a foreign-key relationship.

---

### 🌆 City Management

* Create city
* View all cities
* View city by ID
* Update city
* Delete city

Cities are maintained as a separate master table and linked to employees.

---

## 🖥️ Streamlit User Interface

The project includes a Streamlit frontend located inside the `streamlit_ui` directory.

The interface contains:

* 🔐 Login page
* 📊 Dashboard
* 👨‍💼 Employees
* 🏢 Departments
* 💼 Designations
* 🌆 Cities
* 🚪 Logout functionality

The dashboard displays counts for:

* Total Employees
* Total Departments
* Total Designations
* Total Cities

The Streamlit application communicates with the FastAPI backend through HTTP requests.

> **Note:** The current Streamlit login uses credentials directly in the application code for demonstration purposes. For production use, authentication should be moved to a secure authentication system and credentials should not be hard-coded.

---

## 🛠️ Technology Stack

| Technology     | Purpose                             |
| -------------- | ----------------------------------- |
| **Python**     | Core programming language           |
| **FastAPI**    | REST API framework                  |
| **SQLAlchemy** | ORM and database interaction        |
| **MySQL**      | Relational database                 |
| **PyMySQL**    | MySQL database driver               |
| **Pydantic**   | Request/response validation         |
| **Uvicorn**    | ASGI server                         |
| **Streamlit**  | Frontend/UI                         |
| **Requests**   | API communication                   |
| **Pandas**     | Data handling/supporting operations |

The repository's dependency file includes FastAPI, SQLAlchemy, MySQL connectors, PyMySQL, Pydantic, Uvicorn, Streamlit-related dependencies, Requests, and Pandas.

---

## 📂 Project Structure

```text
HR_Management_API/
│
├── routers/
│   ├── department.py
│   ├── designation.py
│   ├── city.py
│   └── employee.py
│
├── streamlit_ui/
│   ├── app.py
│   ├── config.py
│   ├── employees.py
│   ├── departments.py
│   ├── designations.py
│   └── cities.py
│
├── crud.py
├── database.py
├── main.py
├── models.py
├── schemas.py
├── seed_data.py
├── test_db.py
├── requirements.txt
└── .gitignore
```

The repository currently contains separate router modules and a dedicated Streamlit UI directory.

---

# 🗄️ Database Design

The application uses **MySQL** with **SQLAlchemy ORM**.

### Main Tables

```text
Department
    │
    │ 1
    │
    │ N
Employee
    │
    ├────────── N : 1 ────────── Designation
    │
    └────────── N : 1 ────────── City
```

### Department

| Column          | Type    | Description     |
| --------------- | ------- | --------------- |
| department_id   | Integer | Primary Key     |
| department_name | String  | Department name |

### Designation

| Column           | Type    | Description      |
| ---------------- | ------- | ---------------- |
| designation_id   | Integer | Primary Key      |
| designation_name | String  | Designation name |

### City

| Column    | Type    | Description |
| --------- | ------- | ----------- |
| city_id   | Integer | Primary Key |
| city_name | String  | City name   |

### Employee

| Column         | Type    | Description   |
| -------------- | ------- | ------------- |
| emp_id         | Integer | Primary Key   |
| emp_name       | String  | Employee name |
| age            | Integer | Employee age  |
| salary         | Integer | Salary        |
| joining_date   | Date    | Joining date  |
| department_id  | Integer | Foreign Key   |
| designation_id | Integer | Foreign Key   |
| city_id        | Integer | Foreign Key   |

These relationships and fields are defined in the SQLAlchemy models.

---

# 🔌 API Endpoints

Base URL:

```text
http://127.0.0.1:8000
```

## 👨‍💼 Employees

| Method | Endpoint              | Description             |
| ------ | --------------------- | ----------------------- |
| POST   | `/employees/`         | Create employee         |
| GET    | `/employees/`         | Get employees           |
| GET    | `/employees/search/`  | Search/filter employees |
| GET    | `/employees/{emp_id}` | Get employee by ID      |
| PUT    | `/employees/{emp_id}` | Update employee         |
| DELETE | `/employees/{emp_id}` | Delete employee         |

The employee search endpoint supports filtering by employee name, department, designation, and city. The employee list also supports `skip` and `limit` parameters.

### Example

```http
GET /employees/?skip=0&limit=100
```

Search:

```http
GET /employees/search/?name=John
```

Filter:

```http
GET /employees/search/?department_id=1
```

---

## 🏢 Departments

| Method | Endpoint                       | Description          |
| ------ | ------------------------------ | -------------------- |
| POST   | `/departments/`                | Create department    |
| GET    | `/departments/`                | Get all departments  |
| GET    | `/departments/{department_id}` | Get department by ID |
| PUT    | `/departments/{department_id}` | Update department    |
| DELETE | `/departments/{department_id}` | Delete department    |

---

## 💼 Designations

| Method | Endpoint                         | Description           |
| ------ | -------------------------------- | --------------------- |
| POST   | `/designations/`                 | Create designation    |
| GET    | `/designations/`                 | Get all designations  |
| GET    | `/designations/{designation_id}` | Get designation by ID |
| PUT    | `/designations/{designation_id}` | Update designation    |
| DELETE | `/designations/{designation_id}` | Delete designation    |

---

## 🌆 Cities

| Method | Endpoint            | Description    |
| ------ | ------------------- | -------------- |
| POST   | `/cities/`          | Create city    |
| GET    | `/cities/`          | Get all cities |
| GET    | `/cities/{city_id}` | Get city by ID |
| PUT    | `/cities/{city_id}` | Update city    |
| DELETE | `/cities/{city_id}` | Delete city    |

---

# 📋 Data Validation

Pydantic schemas are used to validate incoming API data.

Employee validation includes:

* Employee name: 2–100 characters
* Age: 18–60
* Salary: greater than 0
* Joining date: valid date
* Department ID: greater than 0
* Designation ID: greater than 0
* City ID: greater than 0

Department, designation, and city names are also validated for length.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/aakashset/HR_Management_API.git
```

Move into the project:

```bash
cd HR_Management_API
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ MySQL Configuration

Create a MySQL database:

```sql
CREATE DATABASE hr_management;
```

Configure the database connection using an environment variable rather than storing database credentials directly in source code.

Example:

```text
DATABASE_URL=mysql+pymysql://username:password@localhost/hr_management
```

Then configure the application to read `DATABASE_URL`.

> ⚠️ Never commit real database passwords, API keys, tokens, or other secrets to GitHub.

---

# 🌱 Seed Data

The project contains a `seed_data.py` script for inserting initial master data into the database.

Run:

```bash
python seed_data.py
```

The seed script includes sample department data and creates related master records.

---

# 🚀 Running the FastAPI Application

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

The FastAPI application registers all four resource routers and exposes a root health/message endpoint.

---

# 🖥️ Running the Streamlit Application

Open another terminal and move into the UI directory:

```bash
cd streamlit_ui
```

Run:

```bash
streamlit run app.py
```

The Streamlit application connects to the FastAPI server using:

```text
http://127.0.0.1:8000
```

This URL is currently configured in `streamlit_ui/config.py`.

---

# 🔄 Application Workflow

```text
User
 │
 ▼
Streamlit Web Application
 │
 │ HTTP Requests
 ▼
FastAPI
 │
 ├── Employee Router
 ├── Department Router
 ├── Designation Router
 └── City Router
 │
 ▼
CRUD Operations
 │
 ▼
SQLAlchemy ORM
 │
 ▼
MySQL Database
```

---

# 🧪 Testing

The project includes:

```text
test_db.py
```

for database-related testing/checking.

API endpoints can also be tested through FastAPI's built-in Swagger interface:

```text
http://127.0.0.1:8000/docs
```

---

# 📊 Dashboard

The Streamlit dashboard provides an overview of the HR data with four primary metrics:

```text
┌───────────────┬────────────────┬────────────────┬──────────────┐
│   Employees   │  Departments   │  Designations  │    Cities    │
└───────────────┴────────────────┴────────────────┴──────────────┘
```

The dashboard retrieves these values directly from the FastAPI endpoints.

---

# 🔐 Security Note

This project is intended primarily as a learning/portfolio application.

For production deployment, the following improvements are recommended:

* Use environment variables for database credentials
* Implement secure authentication
* Hash passwords
* Add authorization and role-based access control
* Add API authentication such as JWT
* Configure CORS appropriately
* Add centralized exception handling
* Add logging
* Validate and sanitize production inputs
* Use HTTPS
* Never commit `.env` files or secrets

---

# 🚀 Future Enhancements

Possible improvements include:

* 🔐 JWT authentication
* 👤 Role-based access control
* 📧 Email notifications
* 📅 Attendance management
* 🏖️ Leave management
* 💰 Payroll management
* 📊 Advanced HR analytics
* 🔎 Advanced employee filtering
* 📄 Export employee reports
* ☁️ Cloud deployment
* 🐳 Docker support
* 🧪 Automated API tests
* 🔄 CI/CD pipeline

---

# 👨‍💻 Author

**Aakash**

Python / Data Engineering Enthusiast

---

# ⭐ Project

If you find this project useful, feel free to ⭐ star the repository.

**GitHub Repository:**
https://github.com/aakashset/HR_Management_API
