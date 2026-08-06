import streamlit as st
import pandas as pd
import requests
from config import API_URL

def employees_page():
    dept_response = requests.get(f"{API_URL}/departments")
    des_response = requests.get(f"{API_URL}/designations")
    city_response = requests.get(f"{API_URL}/cities")

    departments = dept_response.json()
    designations = des_response.json()
    cities = city_response.json()
    st.title(" Employee Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        " View Employees",
        " Add Employee",
        " Update Employee",
        " Delete Employee"
    ])


# VIEW EMPLOYEES


    with tab1:

     response = requests.get(f"{API_URL}/employees")

    if response.status_code == 200:

        employees = response.json()

        df = pd.DataFrame(employees)

        if not df.empty:

            df = df.rename(columns={
                "emp_id": "ID",
                "emp_name": "Name",
                "age": "Age",
                "salary": "Salary",
                "joining_date": "Joining Date"
            })

            df["Department"] = df["department"].apply(
                lambda x: x["department_name"]
            )

            df["Designation"] = df["designation"].apply(
                lambda x: x["designation_name"]
            )

            df["City"] = df["city"].apply(
                lambda x: x["city_name"]
            )

            df = df[
                [
                    "ID",
                    "Name",
                    "Age",
                    "Salary",
                    "Joining Date",
                    "Department",
                    "Designation",
                    "City"
                ]
            ]

            search = st.text_input(
                " Search Employee"
            )

            if search:
                df = df[
                    df["Name"].str.contains(
                        search,
                        case=False
                    )
                ]

            st.dataframe(
                df,
                use_container_width=True
            )

        else:
            st.warning(
                "No Employees Found."
            )

    else:
        st.error(
            "Cannot connect to API"
        )

    # ======================================
    # ADD EMPLOYEE
    # ======================================

    with tab2:

        st.subheader(" Add Employee")

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Employee Name",
                key="add_name"
            )

            age = st.number_input(
                "Age",
                min_value=18,
                max_value=60,
                key="add_age"
            )

            salary = st.number_input(
                "Salary",
                min_value=1000,
                key="add_salary"
            )

        with col2:

            joining_date = st.date_input(
                "Joining Date",
                key="add_joining"
            )

            department = st.selectbox(
                "Department",
                departments,
                format_func=lambda x: x["department_name"],
                key="add_department"
            )

            designation = st.selectbox(
                "Designation",
                designations,
                format_func=lambda x: x["designation_name"],
                key="add_designation"
            )

            city = st.selectbox(
                "City",
                cities,
                format_func=lambda x: x["city_name"],
                key="add_city"
            )

        if st.button(
                " Save Employee",
                use_container_width=True
        ):

            employee = {
                "emp_name": name,
                "age": age,
                "salary": salary,
                "joining_date": str(joining_date),
                "department_id": department["department_id"],
                "designation_id": designation["designation_id"],
                "city_id": city["city_id"]
            }

            response = requests.post(
                f"{API_URL}/employees/",
                json=employee
            )

            if response.status_code in [200, 201]:
                st.success(" Employee Added Successfully")
                st.rerun()
            else:
                st.error(response.text)

# ======================================
# UPDATE EMPLOYEE
# ======================================

    with tab3:

     st.subheader(" Update Employee")

    update_id = st.number_input(
        "Employee ID",
        min_value=1,
        key="update_id"
    )

    update_name = st.text_input(
        "Employee Name",
        key="update_name"
    )

    update_age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        key="update_age"
    )

    update_salary = st.number_input(
        "Salary",
        min_value=1000,
        key="update_salary"
    )

    update_joining = st.date_input(
        "Joining Date",
        key="update_joining"
    )

    update_department = st.number_input(
        "Department ID",
        min_value=1,
        key="update_department"
    )

    update_designation = st.number_input(
        "Designation ID",
        min_value=1,
        key="update_designation"
    )

    update_city = st.number_input(
        "City ID",
        min_value=1,
        key="update_city"
    )

    if st.button("Update Employee", key="update_button"):

        employee = {
            "emp_name": update_name,
            "age": update_age,
            "salary": update_salary,
            "joining_date": str(update_joining),
            "department_id": update_department,
            "designation_id": update_designation,
            "city_id": update_city
        }

        response = requests.put(
            f"{API_URL}/employees/{update_id}",
            json=employee
        )

        if response.status_code == 200:
            st.success(" Employee Updated Successfully")
            st.rerun()
        else:
            st.error(response.text)



# DELETE EMPLOYEE


    with tab4:

     st.subheader(" Delete Employee")

    delete_id = st.number_input(
        "Employee ID",
        min_value=1,
        key="delete_id"
    )

    if st.button("Delete Employee", key="delete_button"):

        response = requests.delete(
            f"{API_URL}/employees/{delete_id}"
        )

        if response.status_code == 200:
            st.success(" Employee Deleted Successfully")
            st.rerun()
        else:
            st.error(response.text)
