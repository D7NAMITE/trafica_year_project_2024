import streamlit as st
import streamlit_shadcn_ui as ui


st.set_page_config(layout="wide")

st.title("🚥 Trafica - 2024 Year Project")


home_tab, overview_tab = st.tabs(["Home", "Overview"])

with home_tab:
    st.subheader("👋Hi, Welcome to our Project")
    st.markdown("""
    This project is a part of the year project of  ***Data Acquisition and Integration***, 
***Data Analytics***, and ***Software Testing*** course Kasetsart University.

Our project aims to collect data to study the possible effects of traffic around 
Kasetsart University (Computer Department) that potentially cause air/noise pollution.

Our goal is to study the correlations between the acquired data using the 
knowledge on data acquisition and analytics.
    """)

with overview_tab:
    st.subheader("Overview")
    option = st.selectbox(
        'How would you like to be contacted?',
        ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"))

    st.write('You selected:', option)

    data_cols = st.columns(3)

    with data_cols[0]:
        sub_cols_aqi = st.columns(2)
        with sub_cols_aqi[0]:
            ui.metric_card(title="Average AQI", content=f"45", description="AQI-US")
        with sub_cols_aqi[1]:
            ui.metric_card(title="Average PM2.5", content=f"17", description="µg/m³")