import streamlit as st
import pandas as pd
import requests

from config import API_URL


def designations_page():

    st.title(" Designation Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        " View Designations",
        " Add Designation",
        " Update Designation",
        " Delete Designation"
    ])


    # VIEW DESIGNATIONS


    with tab1:

        response = requests.get(f"{API_URL}/designations/")

        if response.status_code == 200:

            designations = response.json()

            df = pd.DataFrame(designations)

            if not df.empty:

                df = df.rename(columns={
                    "designation_id": "ID",
                    "designation_name": "Designation"
                })

                search = st.text_input(
                    "🔍 Search Designation",
                    key="search_designation"
                )

                if search:
                    df = df[
                        df["Designation"].str.contains(
                            search,
                            case=False
                        )
                    ]

                st.dataframe(
                    df,
                    use_container_width=True
                )

            else:
                st.warning("No Designations Found.")

        else:
            st.error("Unable to fetch designations.")


    # ADD DESIGNATION


    with tab2:

        st.subheader(" Add Designation")

        designation_name = st.text_input(
            "Designation Name",
            key="add_designation"
        )

        if st.button(
            "Save Designation",
            key="save_designation"
        ):

            data = {
                "designation_name": designation_name
            }

            response = requests.post(
                f"{API_URL}/designations/",
                json=data
            )

            if response.status_code in [200, 201]:
                st.success("Designation Added Successfully")
                st.rerun()
            else:
                st.error(response.text)


    # UPDATE DESIGNATION


    with tab3:

        st.subheader(" Update Designation")

        designation_id = st.number_input(
            "Designation ID",
            min_value=1,
            key="update_designation_id"
        )

        designation_name = st.text_input(
            "New Designation Name",
            key="update_designation_name"
        )

        if st.button(
            "Update Designation",
            key="update_designation"
        ):

            data = {
                "designation_name": designation_name
            }

            response = requests.put(
                f"{API_URL}/designations/{designation_id}",
                json=data
            )

            if response.status_code == 200:
                st.success("Designation Updated Successfully")
                st.rerun()
            else:
                st.error(response.text)

    # DELETE DESIGNATION


    with tab4:

        st.subheader("🗑 Delete Designation")

        designation_id = st.number_input(
            "Designation ID",
            min_value=1,
            key="delete_designation_id"
        )

        if st.button(
            "Delete Designation",
            key="delete_designation"
        ):

            response = requests.delete(
                f"{API_URL}/designations/{designation_id}"
            )

            if response.status_code == 200:
                st.success("Designation Deleted Successfully")
                st.rerun()
            else:
                st.error(response.text)