
# Trafica - 2024 Year Project

| **GitHub**                                  | **Contributors**         | **Student ID** |
|---------------------------------------------|:-------------------------|:---------------|
| [D7NAMITE](https://github.com/D7NAMITE)     | Nanthawat Duang-ead      | 6510545551     |
| [PhumrapeeC](https://github.com/PhumrapeeC) | Phumrapee Chaowanapricha | 6510545683     |

Software and Knowledge Engineering, Faculty of Engineering, Kasetsart University

## Abstract
This project is a part of the year project of  ***Data Acquisition and Integration***, 
***Data Analytics***, and ***Software Testing*** course Kasetsart University.

Our project aims to collect data to study the possible effects of traffic around 
Kasetsart University (Computer Department) that potentially cause air/noise pollution.

Our goal is to study the correlations between the acquired data using the 
knowledge on data acquisition and analytics.

> By the “traffic around Kasetsart University”, we refer to the traffic on 
**Vibhavadi**, **Phahonyothin**, and **Ngamwongwan** Road which only includes the section 
that’s around the campus area.

## Features
**Trafica web-application would provide the following:**
- Visualize the the acquired Traffic Flow, Air Quality, Noise Pollution data around the Computer Engineering Dept. Kasetsart University
- Display statistical number of the data acquired

**The API would provide:**
Statistical Endpoints of the acquired data included

 **AIR QUALITY**
- Average AQI values
- Average AQI values daywise
- AQI value for the selected day
- Minimum AQI US and the day
- Minimum PM2.5 and the day
- Maximum AQI US and the day
- Maximum PM2.5 and the day
- Average AQI values
- Average AQI values daywise

**SOUND LEVEL**
-  Average sound level
- Average sound level daywise
- Sound level for the selected day
- Minimum sound level and the day
- Maximum sound level and the day

**TRAFFIC FLOW**
-  Average traffic flow of each roads
- Average traffic flow daywise of each roads
- Traffic flow for the selected day of each roads
- Traffic flow for the selected road
- Minimum traffic flow of each roads
- Maximum traffic flow of each roads

## Libraries and Tools
**Python**
We use Python as a main programming language in our project

**Fast API**
We utilized Fast API to create our API Endpoints

**Streamlit**
Streamlit is an open-source Python framework that is focus on developing web-application
[Checkout thier official page here](https://streamlit.io/)

**streamlit_shadcn_ui**
streamlit_shadcn_ui is a package of shadcn_ui component that's available to Streamlit
[Checkout thier GitHub here](https://github.com/ObservedObserver/streamlit-shadcn-ui)

The remaining libraries and tools are available in `requirements.txt` file. 
You can install it by following the instruction in `Setup and Configurations Guide`

## Primary Data Source
- [Sound Meter app](https://play.google.com/store/apps/details?id=com.splendapps.decibel&hl=en&gl=US&pli=1)

## API and Secondary Data Sources
- [Tomtom's Traffic Flow API](https://developer.tomtom.com/traffic-api/documentation/traffic-flow/traffic-flow-service)
- ~~[IQAir Air Quality Service - JANANAN KINDERGARTEN Station](https://www.iqair.com/th/thailand/bangkok/jananan-kindergarten)~~
- [IQAir Air Quality Service - Chatuchak Station](https://www.iqair.com/th/thailand/bangkok/chatuchak)

> ***[Editor Note 26/04/2024 CHANGED ON IQAir API Source]***
> 
> The JANANAN KINDERGARTEN Station has changed the name to Chatuchak Station

## Setup and Configurations Guide
Here is some guideline on how to setup the project:

### Clone the repository
Open the terminal at the desire directory, and run the following command:
```
> git clone https://github.com/D7NAMITE/year_project_2024.git
```

After cloning the project. Navigate to the repository with this command:
```
> cd year_project_2024
```

### Initialize the Virtual Environment
Generate the virtual environment using the following command:

**Windows**
```
> python -m venv venv
```
**MacOS**
```
> python3 -m venv venv
```

Then after the virtual environment is generated, activate the virtual environment
**Windows**
```
> venv/Scripts/activate
```

**MacOS**
```
> source venv/bin/activate
```
Lastly, install the required packages using the following command:
```
> pip install -r requirements.txt
```

*Credit: MacOS guide were originated from this [Medium article][^1]*

[^1]: <https://medium.com/datacat/a-simple-guide-to-creating-a-virtual-environment-in-python-for-windows-and-mac-1079f40be518> "A simple guide to creating a virtual environment in Python for Windows and Mac"

### Configure the `config.py`
1. Duplicate the `config.py.example`. Rename it to `config.py`
2. Fill in the following fields
   - DB_HOST = "[Database Host]"
   - DB_USER = "[KU Nontri Account (b6xxxxxxxxx)]"
   - DB_PASSWD = "[KU Email (@ku.th)]"
   - DB_NAME = "[Database Name]"

### Start an App
> For KU students, make sure that you have turned on the VPN connection to 
> connect to the database

#### To start an API connection
```
> uvicorn app:app --port 8000 --reload
```
You'll be able to access the api endpoints via
```
http://localhost:8000/[api_endpoints]
```

#### To run the application ui
From the project root directory (`../year_project_2024`). Navigate to the 
`ui_elements` directory
```
> cd ui_elements
```

Run the web application by the following command:
```
> streamlit run homepage.py
```

Access the web application via
```
http://localhost:8501
``` 

### To Access the API Specification Documentation
Run the server and route to this path: 

```
http://127.0.0.1:8000/docs
```

The path can be changed due to the port modifications.



