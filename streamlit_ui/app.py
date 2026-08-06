import streamlit as st
import requests

from config import API_URL

from employees import employees_page
from departments import departments_page
from designations import designations_page
from cities import cities_page


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="HR Management System",
    page_icon="🏢",
    layout="wide"
)

# ==========================================
# LOGIN SESSION
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ==========================================
# LOGIN PAGE
# ==========================================

if not st.session_state.logged_in:

    st.title("🔐 HR Management System")
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":

            st.session_state.logged_in = True
            st.session_state.username = username

            st.success("Login Successful!")
            st.rerun()

        else:
            st.error("Invalid Username or Password")

    # Stop the app here until the user logs in
    st.stop()

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🏢 HR Management")

st.sidebar.write(f"Welcome, **{st.session_state.username}**")

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Employees",
        "Departments",
        "Designations",
        "Cities"
    ]
)

# ==========================================
# DASHBOARD
# ==========================================

if menu == "Dashboard":

    st.title("🏢 HR Management Dashboard")

    st.success("Welcome to HR Management System")

    try:

        employees = requests.get(f"{API_URL}/employees").json()
        departments = requests.get(f"{API_URL}/departments").json()
        designations = requests.get(f"{API_URL}/designations").json()
        cities = requests.get(f"{API_URL}/cities").json()

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("Employees", len(employees))

        with c2:
            st.metric("Departments", len(departments))

        with c3:
            st.metric("Designations", len(designations))

        with c4:
            st.metric("Cities", len(cities))

    except Exception:
        st.error("Unable to connect to FastAPI")

# ==========================================
# EMPLOYEES
# ==========================================

elif menu == "Employees":
    employees_page()

# ==========================================
# DEPARTMENTS
# ==========================================

elif menu == "Departments":
    departments_page()

# ==========================================
# DESIGNATIONS
# ==========================================

elif menu == "Designations":
    designations_page()

# ==========================================
# CITIES
# ==========================================

elif menu == "Cities":
    cities_page()