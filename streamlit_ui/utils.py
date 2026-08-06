import requests
from config import API_URL


# ==========================
# EMPLOYEE APIs
# ==========================

def get_employees():
    return requests.get(f"{API_URL}/employees/")


def add_employee(data):
    return requests.post(f"{API_URL}/employees/", json=data)


def update_employee(emp_id, data):
    return requests.put(f"{API_URL}/employees/{emp_id}", json=data)


def delete_employee(emp_id):
    return requests.delete(f"{API_URL}/employees/{emp_id}")


# ==========================
# DEPARTMENT APIs
# ==========================

def get_departments():
    return requests.get(f"{API_URL}/departments/")


def add_department(data):
    return requests.post(f"{API_URL}/departments/", json=data)


# ==========================
# DESIGNATION APIs
# ==========================

def get_designations():
    return requests.get(f"{API_URL}/designations/")


def add_designation(data):
    return requests.post(f"{API_URL}/designations/", json=data)


# ==========================
# CITY APIs
# ==========================

def get_cities():
    return requests.get(f"{API_URL}/cities/")


def add_city(data):
    return requests.post(f"{API_URL}/cities/", json=data)