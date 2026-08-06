import streamlit as st
import pandas as pd
import requests

from config import API_URL


def cities_page():

    st.title("🌆 City Management")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 View Cities",
        "➕ Add City",
        "✏️ Update City",
        "🗑 Delete City"
    ])

    # =====================================
    # VIEW CITIES
    # =====================================

    with tab1:

        response = requests.get(f"{API_URL}/cities/")

        if response.status_code == 200:

            cities = response.json()

            df = pd.DataFrame(cities)

            if not df.empty:

                df = df.rename(columns={
                    "city_id": "ID",
                    "city_name": "City"
                })

                search = st.text_input(
                    "🔍 Search City",
                    key="search_city"
                )

                if search:
                    df = df[
                        df["City"].str.contains(
                            search,
                            case=False
                        )
                    ]

                st.dataframe(
                    df,
                    use_container_width=True
                )

            else:
                st.warning("No Cities Found.")

        else:
            st.error("Unable to fetch cities.")

    # =====================================
    # ADD CITY
    # =====================================

    with tab2:

        st.subheader("➕ Add City")

        city_name = st.text_input(
            "City Name",
            key="add_city"
        )

        if st.button(
            "Save City",
            key="save_city"
        ):

            data = {
                "city_name": city_name
            }

            response = requests.post(
                f"{API_URL}/cities/",
                json=data
            )

            if response.status_code in [200, 201]:
                st.success("City Added Successfully")
                st.rerun()
            else:
                st.error(response.text)

    # =====================================
    # UPDATE CITY
    # =====================================

    with tab3:

        st.subheader("✏️ Update City")

        city_id = st.number_input(
            "City ID",
            min_value=1,
            key="update_city_id"
        )

        city_name = st.text_input(
            "New City Name",
            key="update_city_name"
        )

        if st.button(
            "Update City",
            key="update_city"
        ):

            data = {
                "city_name": city_name
            }

            response = requests.put(
                f"{API_URL}/cities/{city_id}",
                json=data
            )

            if response.status_code == 200:
                st.success("City Updated Successfully")
                st.rerun()
            else:
                st.error(response.text)

    # =====================================
    # DELETE CITY
    # =====================================

    with tab4:

        st.subheader("🗑 Delete City")

        city_id = st.number_input(
            "City ID",
            min_value=1,
            key="delete_city_id"
        )

        if st.button(
            "Delete City",
            key="delete_city"
        ):

            response = requests.delete(
                f"{API_URL}/cities/{city_id}"
            )

            if response.status_code == 200:
                st.success("City Deleted Successfully")
                st.rerun()
            else:
                st.error(response.text)