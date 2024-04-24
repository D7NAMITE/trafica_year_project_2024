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


class NoiseValues(BaseModel):
    date: datetime
    dB: float


class TrafficValues(BaseModel):
    date: datetime
    sector: int
    curr_speed: float
    freeflow_speed: float
    road_closure: int


@app.get("/api/aqi/avg/daily")
async def get_daily_avg_aqi() -> list[AQIValues]:
    """Return daily average air quality values included Air Quality Index,
    PM2.5 (in microgram/cubic meter).
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


@app.get("/api/aqi/day/{day_id}")
async def get_day_aqi(day_id: int) -> list[AQIValues]:
    """Return selected day air quality values included Air Quality Index,
    PM2.5 (in microgram/cubic meter).
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
        if not result:
            raise HTTPException(status_code=404,
                                detail="[AQI] Data in the day not found")
    return result


@app.get("/api/noise/avg/daily")
async def get_daily_avg_noise() -> list[NoiseValues]:
    """Return average noise value of each day in decibel"""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT DATE(TS) as date,
            AVG(AVG) as dB
            FROM YP_NOISE
            GROUP BY date;
        """)
        result = [NoiseValues(date=DATE, dB=dB) for DATE, dB in cs.fetchall()]
    return result


@app.get("/api/noise/day/{day_id}")
async def get_day_noise(day_id: int) -> list[NoiseValues]:
    """Return selected day noise value included noise in dB."""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT TS,
            AVG
            FROM YP_NOISE
            WHERE DAYOFWEEK(TS)=%s
        """, [day_id])
        result = [NoiseValues(date=DATE, dB=AVG)
                  for DATE, AVG in cs.fetchall()]
        if not result:
            raise HTTPException(status_code=404,
                                detail="[Noise] Data in the day not found")
    return result


@app.get('/api/traffic/avg/daily')
async def get_daily_avg_traffic() -> list[TrafficValues]:
    """Return average daily traffic"""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT DATE(TS) as date, 
            sector, 
            AVG(currSpeed), 
            AVG(freeFlowSpeed), 
            SUM(roadClosure)
            FROM YP_TRAFFIC
            GROUP BY date, sector
        """)
        result = [TrafficValues(date=DATE,
                                sector=sector,
                                curr_speed=currSpeed,
                                freeflow_speed=freeFlowSpeed,
                                road_closure=roadClosure
                                )
                  for DATE, sector, currSpeed, freeFlowSpeed, roadClosure in cs.fetchall()]
    return result

@app.get('/api/traffic/day/{day_id}')
async def get_day_traffic(day_id: int):
    """Return traffic values for a selected day"""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
        SELECT TS as date, 
        sector, 
        AVG(currSpeed), 
        AVG(freeFlowSpeed), 
        SUM(roadClosure)
        FROM YP_TRAFFIC
        WHERE DAYOFWEEK(TS)=%s
        GROUP BY date, sector
        """, [day_id])
        result = [TrafficValues(date=DATE,
                                sector=sector,
                                curr_speed=currSpeed,
                                freeflow_speed=freeFlowSpeed,
                                road_closure=roadClosure
                                )
                  for DATE, sector, currSpeed, freeFlowSpeed, roadClosure in cs.fetchall()]
        if not result:
            raise HTTPException(status_code=404,
                                detail= "[Traffic] Data in the day not found")
    return result
