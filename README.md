﻿# Trafica - 2024 Year Project

| Author                   |
|--------------------------|
| Nanthawat Duang-ead      |
| Phumrapee Chaowanapricha |

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
- [IQAir Air Quality Service - JANANAN KINDERGARTEN Station](https://www.iqair.com/th/thailand/bangkok/jananan-kindergarten)

## Setup and Configurations Guide
Here is some guideline on how to setup the project:

### Clone the repository
Open the terminal at the desire directory, and run the following command:
```
> git clone https://github.com/D7NAMITE/year_project_2024.git
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

*Credit: MacOS guide were originated from this Medium article[^1]*

### Configure the `config.py`
1. Duplicate the `config.py.example`. Rename it to `config.py`
2. Fill in the following fields
   - DB_HOST = "[Database Host]"
   - DB_USER = "[KU Nontri Account (b6xxxxxxxxx)]"
   - DB_PASSWD = "[KU Email (@ku.th)]"
   - DB_NAME = "[Database Name]"

### To start an app
```
> uvicorn hello:app --port 8000 --reload
```
You'll be able to access the api endpoints via
```
http://localhost:8000/[api_endpoints]
```


[^1]: <https://medium.com/datacat/a-simple-guide-to-creating-a-virtual-environment-in-python-for-windows-and-mac-1079f40be518> "A simple guide to creating a virtual environment in Python for Windows and Mac"
