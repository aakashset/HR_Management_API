import streamlit as st
import pandas as pd
import requests

from config import API_URL


def departments_page():

    st.title(" Department Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        " View Departments",
        " Add Department",
        " Update Department",
        " Delete Department"
    ])


    # VIEW DEPARTMENTS


    with tab1:

        response = requests.get(f"{API_URL}/departments/")

        if response.status_code == 200:

            departments = response.json()

            df = pd.DataFrame(departments)

            if not df.empty:

                df = df.rename(columns={
                    "department_id": "ID",
                    "department_name": "Department"
                })

                search = st.text_input(
                    " Search Department",
                    key="search_department"
                )

                if search:
                    df = df[
                        df["Department"].str.contains(
                            search,
                            case=False
                        )
                    ]

                st.dataframe(
                    df,
                    use_container_width=True
                )

            else:
                st.warning("No Departments Found.")

        else:
            st.error("Unable to fetch departments.")


    # ADD DEPARTMENT


    with tab2:

        st.subheader(" Add Department")

        department_name = st.text_input(
            "Department Name",
            key="add_department"
        )

        if st.button(
            "Save Department",
            key="save_department"
        ):

            data = {
                "department_name": department_name
            }

            response = requests.post(
                f"{API_URL}/departments/",
                json=data
            )

            if response.status_code in [200, 201]:
                st.success("Department Added Successfully")
                st.rerun()
            else:
                st.error(response.text)

    # UPDATE DEPARTMENT


    with tab3:

        st.subheader(" Update Department")

        department_id = st.number_input(
            "Department ID",
            min_value=1,
            key="update_department_id"
        )

        department_name = st.text_input(
            "New Department Name",
            key="update_department_name"
        )

        if st.button(
            "Update Department",
            key="update_department"
        ):

            data = {
                "department_name": department_name
            }

            response = requests.put(
                f"{API_URL}/departments/{department_id}",
                json=data
            )

            if response.status_code == 200:
                st.success("Department Updated Successfully")
                st.rerun()
            else:
                st.error(response.text)


    # DELETE DEPARTMENT


    with tab4:

        st.subheader("🗑 Delete Department")

        department_id = st.number_input(
            "Department ID",
            min_value=1,
            key="delete_department_id"
        )

        if st.button(
            "Delete Department",
            key="delete_department"
        ):

            response = requests.delete(
                f"{API_URL}/departments/{department_id}"
            )

            if response.status_code == 200:
                st.success("Department Deleted Successfully")
                st.rerun()
            else:
                st.error(response.text)