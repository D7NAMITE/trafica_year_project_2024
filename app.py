import pymysql
from dbutils.pooled_db import PooledDB
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME
from datetime import datetime

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)

app = FastAPI()


class AQIValues(BaseModel):
    date: datetime
    aqi_us: float
    pm25: float


@app.get("/aqi/avg/daily")
async def get_daily_avg_aqi() -> list[AQIValues]:
    """
    Return daily average air quality values included Air Quality Index,
    PM2.5 (in microgram/cubic meter).
    :return: List of AQIValues contained daily average values
    """
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT DATE(TS) as date, 
            AVG(AQI_US) as AVG_AQI_US, 
            AVG(PM25) as AVG_PM25 
            FROM YP_AQI 
            GROUP BY date;
        """)
        result = [AQIValues(date=DATE, aqi_us=AQI_US, pm25=PM25)
                  for DATE, AQI_US, PM25 in cs.fetchall()]
    return result


@app.get("/aqi/day/{day_id}")
async def get_day_aqi(day_id: int) -> list[AQIValues]:
    """
    Return selected day air quality values included Air Quality Index,
    PM2.5 (in microgram/cubic meter).
    :param day_id: ID for day in the week. 1=Sunday, 2=Monday, 3=Tuesday,
    4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday.
    :return: List of AQIValues contain aqi values in the selected day
    """
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT TS,
            AQI_US,
            PM25
            FROM YP_AQI
            WHERE DAYOFWEEK(TS)=%s
        """, [day_id])
        result = [AQIValues(date=DATE, aqi_us=AQI_US, pm25=PM25)
                  for DATE, AQI_US, PM25 in cs.fetchall()]
    return result

