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
    st.markdown("## 📈 Overview")

    # TODO: Implement Graph combine every data

    st.markdown("## 🔬 Statistical Figures")

    with st.expander("AQI-US"):
        sub_cols_aqi = st.columns(3)
        with sub_cols_aqi[0]:
            ui.metric_card(title="Average AQI-US",
                           content=f"{45} AQI-US",
                           description="From 15 - 28 May 2024")
        with sub_cols_aqi[1]:
            ui.metric_card(title="Minimum AQI-US",
                           content=f"{45} AQI-US",
                           # TODO: implement date time for description
                           description=f"From {1}")
        with sub_cols_aqi[2]:
            ui.metric_card(title="Maximum AQI-US",
                           content=f"{45} AQI-US",
                           # TODO: implement date time for description
                           description=f"From {2}")

    with st.expander("PM2.5"):
        sub_cols_pm25 = st.columns(3)
        with sub_cols_pm25[0]:
            ui.metric_card(title="Average PM2.5",
                           content=f"{17} µg/m³",
                           description="From 15 - 28 May 2024")
        with sub_cols_pm25[1]:
            ui.metric_card(title="Minimum PM2.5",
                           content=f"{17} µg/m³",
                           # TODO: implement date time for description
                           description=f"From {1}")
        with sub_cols_pm25[2]:
            ui.metric_card(title="Maximum PM2.5",
                           content=f"{17} µg/m³",
                           # TODO: implement date time for description
                           description=f"From {2}")

    with st.expander("Sound Level"):
        sub_cols_noise = st.columns(3)
        with sub_cols_noise[0]:
            ui.metric_card(title="Average Sound Level",
                           content=f"{17} dB",
                           description="From 15 - 28 May 2024")
        with sub_cols_noise[1]:
            ui.metric_card(title="Minimum Sound Level",
                           content=f"{17} dB",
                           # TODO: implement date time for description
                           description=f"From {1}")
        with sub_cols_noise[2]:
            ui.metric_card(title="Maximum Sound Level",
                           content=f"{17} dB",
                           # TODO: implement date time for description
                           description=f"From {2}")

    with st.expander("Vibhavadi Rd."):
        sub_cols_traffic_vibha = st.columns(3)
        with sub_cols_traffic_vibha[0]:
            ui.metric_card(title="Average Vibhavadi Rd. Traffic",
                           content=f"{55} KM/H",
                           description="From 15 - 28 May 2024")
        with sub_cols_traffic_vibha[1]:
            ui.metric_card(title="Average Vibhavadi Rd. Traffic",
                           content=f"{55}",
                           # TODO: implement date time for description
                           description=f"From {1}")
        with sub_cols_traffic_vibha[2]:
            ui.metric_card(title="Average Vibhavadi Rd. Traffic",
                           content=f"{55} KM/H",
                           # TODO: implement date time for description
                           description=f"From {1}")

    with st.expander("Ngamwongwan Rd."):
        sub_cols_traffic_ngam = st.columns(3)
        with sub_cols_traffic_ngam[0]:
            ui.metric_card(title="Average Ngamwongwan Rd. Traffic",
                           content=f"{55} KM/H",
                           description="From 15 - 28 May 2024")
        with sub_cols_traffic_ngam[1]:
            ui.metric_card(title="Minimum Ngamwongwan Rd. Traffic",
                           content=f"{55} KM/H",
                           # TODO: implement date time for description
                           description=f"From {1}")
        with sub_cols_traffic_ngam[2]:
            ui.metric_card(title="Maximum Ngamwongwan Rd. Traffic",
                           content=f"{55} KM/H",
                           # TODO: implement date time for description
                           description=f"From {1}")

    with st.expander("Phahonyothin Rd."):
        sub_cols_traffic_phahon = st.columns(3)
        with sub_cols_traffic_phahon[0]:
            ui.metric_card(title="Average Phahonyothin Rd. Traffic",
                           content=f"{55} KM/H",
                           description="From 15 - 28 May 2024")
        with sub_cols_traffic_phahon[1]:
            ui.metric_card(title="Minimum Phahonyothin Rd. Traffic",
                           content=f"{55} KM/H",
                           # TODO: implement date time for description
                           description=f"From {1}")
        with sub_cols_traffic_phahon[2]:
            ui.metric_card(title="Maximum Phahonyothin Rd. Traffic",
                           content=f"{55} KM/H",
                           # TODO: implement date time for description
                           description=f"From {1}")
