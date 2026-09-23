# 🏢 HR Management System

A full-stack **Human Resource Management System** built using **FastAPI, SQLAlchemy, MySQL, and Streamlit**.

The application provides RESTful APIs and an interactive Streamlit interface for managing **employees, departments, designations, and cities**.

---

## 📌 Project Overview

This project demonstrates how a backend REST API can be integrated with a frontend application and a relational database.

The system follows a modular architecture where:

- **Streamlit** provides the user interface
- **FastAPI** handles REST API requests
- **CRUD layer** manages database operations
- **SQLAlchemy** provides ORM functionality
- **MySQL** stores the application data

---

## 🔄 End-to-End Project Flow

```text
                         👤 User
                           │
                           ▼
                  🖥️ Streamlit UI
                           │
                     HTTP Requests
                           │
                           ▼
                  ⚡ FastAPI Backend
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        Employees     Departments   Designations
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                     🔄 CRUD Layer
                           │
                           ▼
                   🗃️ SQLAlchemy ORM
                           │
                           ▼
                      🐬 MySQL
                           │
                           ▼
                    Data Response
                           │
                           ▼
                  🖥️ Streamlit UI
