# Trafica - 2024 Year Project

| **GitHub**                                  | **Contributors**         |
|---------------------------------------------|:-------------------------|
| [D7NAMITE](https://github.com/D7NAMITE)     | Nanthawat Duang-ead      |
| [PhumrapeeC](https://github.com/PhumrapeeC) | Phumrapee Chaowanapricha |

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
**For KU students, make sure that you have turned on the VPN connection**
```
> uvicorn app:app --port 8000 --reload
```
You'll be able to access the api endpoints via
```
http://localhost:8000/[api_endpoints]
```

### To Access the API Documentation
Run the server and route to this path: `http://127.0.0.1:8000/docs`

The path can be changed due to the port modifications.


