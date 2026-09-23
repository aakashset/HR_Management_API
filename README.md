# 🏢 HR Management System

A full-stack **HR Management System** built using **FastAPI, SQLAlchemy, MySQL, and Streamlit**.

The application provides REST APIs and a Streamlit web interface for managing employees, departments, designations, and cities.

---

## 📌 Project Overview

This project demonstrates a modular HR management application with:

- RESTful APIs using FastAPI
- MySQL database
- SQLAlchemy ORM
- Pydantic data validation
- CRUD operations
- Streamlit web interface
- Employee search and filtering
- Interactive HR dashboard

### Architecture

```text
                    ┌─────────────────────┐
                    │    Streamlit UI     │
                    │    Web Interface    │
                    └──────────┬──────────┘
                               │
                          HTTP Requests
                               │
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │      REST API       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    CRUD Operations  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     SQLAlchemy      │
                    │        ORM          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       MySQL         │
                    │      Database       │
                    └─────────────────────┘
