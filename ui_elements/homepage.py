import pandas as pd
import requests
import streamlit_shadcn_ui as ui
import streamlit as st

ENDPOINT_MAX_TRAFFIC = "http://127.0.0.1:8000/api/traffic/max"
ENDPOINT_MIN_TRAFFIC = "http://127.0.0.1:8000/api/traffic/min"
ENDPOINT_AVG_TRAFFIC = "http://127.0.0.1:8000/api/traffic/avg"
ENDPOINT_MAX_NOISE = "http://127.0.0.1:8000/api/noise/max"
ENDPOINT_MIN_NOISE = "http://127.0.0.1:8000/api/noise/min"
ENDPOINT_AVG_NOISE = "http://127.0.0.1:8000/api/noise/avg"
ENDPOINT_MAX_PM25 = "http://127.0.0.1:8000/api/aqi/max/pm25"
ENDPOINT_MIN_PM25 = "http://127.0.0.1:8000/api/aqi/min/pm25"
ENDPOINT_MAX_AQI_US = "http://127.0.0.1:8000/api/aqi/max/aqi_us"
ENDPOINT_MIN_AQI_US = "http://127.0.0.1:8000/api/aqi/min/aqi_us"
ENDPOINT_AVG_AQI = "http://127.0.0.1:8000/api/aqi/avg"


def get_data(endpoint):
    data = requests.get(endpoint).json()
    df = pd.DataFrame([data])
    df["date"] = pd.to_datetime(df["date"])
    return df


st.set_page_config(layout="wide")


st.title("🚥 Trafica - 2024 Year Project")


home_tab, overview_tab = st.tabs(["Home", "Overview"])

with home_tab:
    st.header("👋Hi, Welcome to our Project")
    st.markdown(
        """
    This project is a part of the year project of  ***Data Acquisition and Integration***, 
***Data Analytics***, and ***Software Testing*** course Kasetsart University.

Our project aims to collect data to study the possible effects of traffic around 
Kasetsart University (Computer Department) that potentially cause air/noise pollution.

Our goal is to study the correlations between the acquired data using the 
knowledge on data acquisition and analytics.
    """
    )

    st.header("🗃️ Project Archive")
    st.markdown("* [GitHub repository](https://github.com/D7NAMITE/year_project_2024)")

    st.header("🔍️Data Sources")
    st.markdown(
        """
    ### Primary Data Source
- [Sound Meter app](https://play.google.com/store/apps/details?id=com.splendapps.decibel&hl=en&gl=US&pli=1)

### API and Secondary Data Sources
- [Tomtom's Traffic Flow API](https://developer.tomtom.com/traffic-api/documentation/traffic-flow/traffic-flow-service)
- [IQAir Air Quality Service - Chatuchak Station](https://www.iqair.com/th/thailand/bangkok/chatuchak)

> ***[Editor Note 26/04/2024 CHANGED ON IQAir API Source]***
> 
> The JANANAN KINDERGARTEN Station has changed the name to Chatuchak Station
    """
    )

    st.header("👨‍💻 Our Team")
    profile_cols = st.columns(2)

    with profile_cols[0]:
        boom_container = st.container(border=True)
        with boom_container:
            st.markdown("### D7NAMITE")
            st.image(image="images/boom_profile_image.jpg", width=200)
            st.markdown("**Nanthawat Duang-ead**")
            st.text(
                "Software and Knowledge Engineering student at Kasetsart University"
            )

    with profile_cols[1]:
        p_container = st.container(border=True)
        with p_container:
            st.subheader("PhumrapeeC")
            st.image(image="images/p_profile_image.jpg", width=200)
            st.markdown("**Phumrapee Chaowanapricha**")
            st.text(
                "Software and Knowledge Engineering student at Kasetsart University"
            )


with (((overview_tab))):
    st.markdown("## 🔎 Overview")
    daily_aqi = requests.get("http://127.0.0.1:8000/api/aqi/avg/daily").json()
    df_daily_aqi = pd.DataFrame(daily_aqi)
    df_daily_aqi["date"] = pd.to_datetime(df_daily_aqi["date"])

    daily_noise = requests.get("http://127.0.0.1:8000/api/noise/avg/daily").json()
    df_daily_noise = pd.DataFrame(daily_noise)
    df_daily_noise["date"] = pd.to_datetime(df_daily_noise["date"])

    daily_traffic = requests.get("http://127.0.0.1:8000/api/traffic/avg/daily").json()
    df_daily_traffic = pd.DataFrame(daily_traffic)
    df_daily_traffic["date"] = pd.to_datetime(df_daily_traffic["date"])

    df_traffic_sector_1 = (df_daily_traffic[df_daily_traffic['sector'] == 1])
    df_traffic_sector_1.rename(columns={'curr_speed': 'Vibhavadi speed'}, inplace=True)
    df_traffic_sector_1 = df_traffic_sector_1.loc[:, ["date", "Vibhavadi speed"]]
    df_traffic_sector_2 = (df_daily_traffic[df_daily_traffic['sector'] == 2])
    df_traffic_sector_2.rename(columns={'curr_speed': 'Ngamwongwan speed'}, inplace=True)
    df_traffic_sector_2 = df_traffic_sector_2.loc[:,["date", "Ngamwongwan speed"]]
    df_traffic_sector_3 = (df_daily_traffic[df_daily_traffic['sector'] == 3])
    df_traffic_sector_3.rename(columns={'curr_speed': 'Phahonyothin speed'}, inplace=True)
    df_traffic_sector_3 = df_traffic_sector_3.loc[:,["date", "Phahonyothin speed"]]
    graph_df = df_traffic_sector_1.merge(df_traffic_sector_2, on='date')
    graph_df = graph_df.merge(df_traffic_sector_3, on='date')
    graph_df = graph_df.merge(df_daily_noise)
    graph_df = graph_df.merge(df_daily_aqi)

    st.line_chart(graph_df, x='date')

    st.markdown("## 🔬 Statistical Figures")

    aqi_avg_df = get_data(ENDPOINT_AVG_AQI)
    aqi_avg_df["date"] = pd.to_datetime(aqi_avg_df["date"])
    avg_aqi_us_date = aqi_avg_df["date"].dt.strftime("%d %B %Y").iloc[0]
    avg_aqi_us_value = round((float(aqi_avg_df["aqi_us"])), 2)
    avg_pm25_value = round((float(aqi_avg_df["pm25"])), 2)

    aqi_min_df = get_data(ENDPOINT_MIN_AQI_US)
    aqi_min_df["date"] = pd.to_datetime(aqi_min_df["date"])
    min_aqi_us_date = aqi_min_df["date"].dt.strftime("%d %B %Y").iloc[0]
    min_aqi_us_value = round((float(aqi_min_df["aqi_us"])), 2)

    aqi_max_df = get_data(ENDPOINT_MAX_AQI_US)
    aqi_max_df["date"] = pd.to_datetime(aqi_max_df["date"])
    max_aqi_us_date = aqi_max_df["date"].dt.strftime("%d %B %Y").iloc[0]
    max_aqi_us_value = round((float(aqi_max_df["aqi_us"])), 2)

    with st.expander("AQI-US"):
        sub_cols_aqi = st.columns(3)
        with sub_cols_aqi[0]:
            ui.metric_card(
                title="Average AQI-US",
                content=f"{avg_aqi_us_value}",
                description=f"Retrieve: {avg_aqi_us_date}",
            )
        with sub_cols_aqi[1]:
            ui.metric_card(
                title="Minimum AQI-US",
                content=f"{min_aqi_us_value}",
                description=f"From {min_aqi_us_date}",
            )
        with sub_cols_aqi[2]:
            ui.metric_card(
                title="Maximum AQI-US",
                content=f"{max_aqi_us_value}",
                description=f"From {max_aqi_us_date}",
            )

    pm25_min_df = get_data(ENDPOINT_MIN_PM25)
    pm25_min_df["date"] = pd.to_datetime(pm25_min_df["date"])
    min_pm25_date = pm25_min_df["date"].dt.strftime("%d %B %Y").iloc[0]
    min_pm25_value = round((float(pm25_min_df["pm25"])), 2)

    pm25_max_df = get_data(ENDPOINT_MAX_PM25)
    pm25_max_df["date"] = pd.to_datetime(pm25_max_df["date"])
    max_pm25_date = pm25_max_df["date"].dt.strftime("%d %B %Y").iloc[0]
    max_pm25_value = round((float(pm25_max_df["pm25"])), 2)

    with st.expander("PM2.5"):
        sub_cols_pm25 = st.columns(3)
        with sub_cols_pm25[0]:
            ui.metric_card(
                title="Average PM2.5",
                content=f"{avg_pm25_value} µg/m³",
                description=f"Retrieve: {avg_aqi_us_date}",
            )
        with sub_cols_pm25[1]:
            ui.metric_card(
                title="Minimum PM2.5",
                content=f"{min_pm25_value} µg/m³",
                description=f"From {min_pm25_date}",
            )

        with sub_cols_pm25[2]:
            ui.metric_card(
                title="Maximum PM2.5",
                content=f"{max_pm25_value} µg/m³",
                description=f"From {max_pm25_date}",
            )

    noise_avg_df = get_data(ENDPOINT_AVG_NOISE)
    noise_avg_df["date"] = pd.to_datetime(noise_avg_df["date"])
    avg_noise_date = noise_avg_df["date"].dt.strftime("%d %B %Y").iloc[0]
    avg_noise_value = round((float(noise_avg_df["dB"])), 2)

    noise_min_df = get_data(ENDPOINT_MIN_NOISE)
    noise_min_df["date"] = pd.to_datetime(noise_min_df["date"])
    min_noise_date = noise_min_df["date"].dt.strftime("%d %B %Y").iloc[0]
    min_noise_value = round((float(noise_min_df["dB"])), 2)

    noise_max_df = get_data(ENDPOINT_MAX_NOISE)
    noise_max_df["date"] = pd.to_datetime(noise_max_df["date"])
    max_noise_date = noise_max_df["date"].dt.strftime("%d %B %Y").iloc[0]
    max_noise_value = round((float(noise_max_df["dB"])), 2)

    with st.expander("Sound Level"):
        sub_cols_noise = st.columns(3)
        with sub_cols_noise[0]:
            ui.metric_card(
                title="Average Sound Level",
                content=f"{avg_noise_value} dB",
                description=f"From {avg_noise_date}",
            )
        with sub_cols_noise[1]:
            ui.metric_card(
                title="Minimum Sound Level",
                content=f"{min_noise_value} dB",
                description=f"From {min_noise_date}",
            )
        with sub_cols_noise[2]:
            ui.metric_card(
                title="Maximum Sound Level",
                content=f"{max_noise_value} dB",
                description=f"From {max_noise_date}",
            )

    avg_traffic_data = requests.get(ENDPOINT_AVG_TRAFFIC).json()
    traffic_avg_df = pd.DataFrame(avg_traffic_data)
    traffic_avg_df["date"] = pd.to_datetime(traffic_avg_df["date"])
    avg_traffic_date = traffic_avg_df["date"].dt.strftime("%d %B %Y").iloc[0]
    avg_curr_speed_sector_1 = round(
        float(traffic_avg_df.loc[traffic_avg_df["sector"] == 1, "curr_speed"]), 2
    )
    avg_curr_speed_sector_2 = round(
        float(traffic_avg_df.loc[traffic_avg_df["sector"] == 2, "curr_speed"]), 2
    )
    avg_curr_speed_sector_3 = round(
        float(traffic_avg_df.loc[traffic_avg_df["sector"] == 3, "curr_speed"]), 2
    )

    min_traffic_data = requests.get(ENDPOINT_MIN_TRAFFIC).json()
    traffic_min_df = pd.DataFrame(min_traffic_data)
    traffic_min_df["date"] = pd.to_datetime(traffic_min_df["date"])
    min_curr_speed_sector_1 = round(
        float(traffic_min_df.loc[traffic_min_df["sector"] == 1, "curr_speed"]), 2
    )
    min_date_sector_1 = (
        traffic_min_df.loc[traffic_min_df["sector"] == 1, "date"]
        .dt.strftime("%d %B %Y")
        .iloc[0]
    )
    min_curr_speed_sector_2 = round(
        float(traffic_min_df.loc[traffic_min_df["sector"] == 2, "curr_speed"]), 2
    )
    min_date_sector_2 = (
        traffic_min_df.loc[traffic_min_df["sector"] == 2, "date"]
        .dt.strftime("%d %B %Y")
        .iloc[0]
    )
    min_curr_speed_sector_3 = round(
        float(traffic_min_df.loc[traffic_min_df["sector"] == 3, "curr_speed"]), 2
    )
    min_date_sector_3 = (
        traffic_min_df.loc[traffic_min_df["sector"] == 3, "date"]
        .dt.strftime("%d %B %Y")
        .iloc[0]
    )

    max_traffic_data = requests.get(ENDPOINT_MAX_TRAFFIC).json()
    traffic_max_df = pd.DataFrame(max_traffic_data)
    traffic_max_df["date"] = pd.to_datetime(traffic_max_df["date"])
    max_curr_speed_sector_1 = round(
        float(traffic_max_df.loc[traffic_max_df["sector"] == 1, "curr_speed"]), 2
    )
    max_date_sector_1 = (
        traffic_max_df.loc[traffic_max_df["sector"] == 1, "date"]
        .dt.strftime("%d %B %Y")
        .iloc[0]
    )
    max_curr_speed_sector_2 = round(
        float(traffic_max_df.loc[traffic_max_df["sector"] == 2, "curr_speed"]), 2
    )
    max_date_sector_2 = (
        traffic_max_df.loc[traffic_max_df["sector"] == 2, "date"]
        .dt.strftime("%d %B %Y")
        .iloc[0]
    )
    max_curr_speed_sector_3 = round(
        float(traffic_max_df.loc[traffic_max_df["sector"] == 3, "curr_speed"]), 2
    )
    max_date_sector_3 = (
        traffic_max_df.loc[traffic_max_df["sector"] == 3, "date"]
        .dt.strftime("%d %B %Y")
        .iloc[0]
    )

    with st.expander("Vibhavadi Rd."):
        sub_cols_traffic_vibha = st.columns(3)
        with sub_cols_traffic_vibha[0]:
            ui.metric_card(
                title="Average Vibhavadi Rd. Traffic",
                content=f"{avg_curr_speed_sector_1} KM/H",
            )
        with sub_cols_traffic_vibha[1]:
            ui.metric_card(
                title="Minimum Vibhavadi Rd. Traffic",
                content=f"{min_curr_speed_sector_1} KM/H",
            )
        with sub_cols_traffic_vibha[2]:
            ui.metric_card(
                title="Maximum Vibhavadi Rd. Traffic",
                content=f"{max_curr_speed_sector_1} KM/H",
            )

    with st.expander("Ngamwongwan Rd."):
        sub_cols_traffic_ngam = st.columns(3)
        with sub_cols_traffic_ngam[0]:
            ui.metric_card(
                title="Average Ngamwongwan Rd. Traffic",
                content=f"{avg_curr_speed_sector_2} KM/H",
            )
        with sub_cols_traffic_ngam[1]:
            ui.metric_card(
                title="Minimum Ngamwongwan Rd. Traffic",
                content=f"{min_curr_speed_sector_2} KM/H",
            )
        with sub_cols_traffic_ngam[2]:
            ui.metric_card(
                title="Maximum Ngamwongwan Rd. Traffic",
                content=f"{max_curr_speed_sector_2} KM/H",
            )

    with st.expander("Phahonyothin Rd."):
        sub_cols_traffic_phahon = st.columns(3)
        with sub_cols_traffic_phahon[0]:
            ui.metric_card(
                title="Average Phahonyothin Rd. Traffic",
                content=f"{avg_curr_speed_sector_3} KM/H",
            )
        with sub_cols_traffic_phahon[1]:
            ui.metric_card(
                title="Minimum Phahonyothin Rd. Traffic",
                content=f"{min_curr_speed_sector_3} KM/H",
            )
        with sub_cols_traffic_phahon[2]:
            ui.metric_card(
                title="Maximum Phahonyothin Rd. Traffic",
                content=f"{max_curr_speed_sector_3} KM/H",
            )
