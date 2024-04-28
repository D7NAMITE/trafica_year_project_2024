import streamlit as st
import streamlit_shadcn_ui as ui


st.set_page_config(layout="wide")

st.title("🚥 Trafica - 2024 Year Project")


home_tab, overview_tab = st.tabs(["Home", "Overview"])

with home_tab:
    st.header("👋Hi, Welcome to our Project")
    st.markdown("""
    This project is a part of the year project of  ***Data Acquisition and Integration***, 
***Data Analytics***, and ***Software Testing*** course Kasetsart University.

Our project aims to collect data to study the possible effects of traffic around 
Kasetsart University (Computer Department) that potentially cause air/noise pollution.

Our goal is to study the correlations between the acquired data using the 
knowledge on data acquisition and analytics.
    """)

    st.header("🗃️ GitHub Repository")
    st.markdown("***Under construction***")

    st.header("🔍️Data Sources")
    st.markdown("""
    ### Primary Data Source
- [Sound Meter app](https://play.google.com/store/apps/details?id=com.splendapps.decibel&hl=en&gl=US&pli=1)

### API and Secondary Data Sources
- [Tomtom's Traffic Flow API](https://developer.tomtom.com/traffic-api/documentation/traffic-flow/traffic-flow-service)
- ~~[IQAir Air Quality Service - JANANAN KINDERGARTEN Station](https://www.iqair.com/th/thailand/bangkok/jananan-kindergarten)~~
- [IQAir Air Quality Service - Chatuchak Station](https://www.iqair.com/th/thailand/bangkok/chatuchak)

> ***[Editor Note 26/04/2024 CHANGED ON IQAir API Source]***
> 
> The JANANAN KINDERGARTEN Station has changed the name to Chatuchak Station
    """)

    st.header("👨‍💻 Our Team")
    profile_cols = st.columns(2)

    with profile_cols[0]:
        boom_container = st.container(border=True)
        with boom_container:
            st.markdown("### D7NAMITE")
            st.image(image="images/boom_profile_image.jpg", width=200)
            st.markdown("**Nanthawat Duang-ead**")
            st.text("Software and Knowledge Engineering student at Kasetsart University")

    with profile_cols[1]:
        p_container = st.container(border=True)
        with p_container:
            st.subheader("PhumrapeeC")
            st.image(image="images/p_profile_image.jpg", width=200)
            st.markdown("**Phumrapee Chaowanapricha**")
            st.text("Software and Knowledge Engineering student at Kasetsart University")



with overview_tab:
    st.subheader("Overview")
    option = st.selectbox(
        'Select the day in the week',
        ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"))


    st.write('You selected:', option)

    data_cols = st.columns(3)

    with data_cols[0]:
        sub_cols_aqi = st.columns(2)
        with sub_cols_aqi[0]:
            ui.metric_card(title="Average AQI", content=f"45", description="AQI-US")
        with sub_cols_aqi[1]:
            ui.metric_card(title="Average PM2.5", content=f"17", description="µg/m³")