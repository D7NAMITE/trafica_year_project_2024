import pymysql
from dbutils.pooled_db import PooledDB
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME
from datetime import datetime

pool = PooledDB(
    creator=pymysql,
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWD,
    database=DB_NAME,
    maxconnections=1,
    blocking=True,
)

app = FastAPI()


class AQIValues(BaseModel):
    date: datetime
    aqi_us: float
    pm25: float


class AQIUsValues(BaseModel):
    date: datetime
    aqi_us: float


class PM25Values(BaseModel):
    date: datetime
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


@app.get("/api/aqi/avg")
async def get_avg_aqi() -> AQIValues:
    """Return the average AQI of the whole dataset included Air Quality Index,
    PM2.5 (in microgram/cubic meter).
    """
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT AVG(AQI_US) as AVG_AQI_US, 
            AVG(PM25) as AVG_PM25 
            FROM YP_AQI;
        """
        )
        result = cs.fetchone()
        AQI_US, PM25 = result
        return AQIValues(date=datetime.now(), aqi_us=AQI_US, pm25=PM25)


@app.get("/api/aqi/avg/daily")
async def get_daily_avg_aqi() -> list[AQIValues]:
    """Return daily average air quality values included Air Quality Index,
    PM2.5 (in microgram/cubic meter).
    """
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT DATE(TS) as date, 
            AVG(AQI_US) as AVG_AQI_US, 
            AVG(PM25) as AVG_PM25 
            FROM YP_AQI 
            GROUP BY date;
        """
        )
        result = [
            AQIValues(date=DATE, aqi_us=AQI_US, pm25=PM25)
            for DATE, AQI_US, PM25 in cs.fetchall()
        ]
    return result


@app.get("/api/aqi/day/{day_id}")
async def get_day_aqi(day_id: int) -> list[AQIValues]:
    """Return selected day air quality values included Air Quality Index,
    PM2.5 (in microgram/cubic meter).
    """
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT TS,
            AQI_US,
            PM25
            FROM YP_AQI
            WHERE DAYOFWEEK(TS)=%s
        """,
            [day_id],
        )
        result = [
            AQIValues(date=DATE, aqi_us=AQI_US, pm25=PM25)
            for DATE, AQI_US, PM25 in cs.fetchall()
        ]
        if not result:
            raise HTTPException(status_code=404, detail="[AQI] Data not found")
    return result


@app.get("/api/aqi/min/aqi_us")
async def get_min_aqi_us() -> AQIUsValues:
    """Return the minimum AQI of the whole dataset included Air Quality Index."""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT 
            TS, 
            AQI_US 
            FROM YP_AQI 
            WHERE AQI_US = (SELECT MIN(AQI_US) FROM YP_AQI);
        """
        )
        result = cs.fetchone()
        DATE, AQI_US = result
        return AQIUsValues(date=DATE, aqi_us=AQI_US)


@app.get("/api/aqi/max/aqi_us")
async def get_max_aqi_us() -> AQIUsValues:
    """Return the maximum AQI of the whole dataset included Air Quality Index."""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT 
            TS, 
            AQI_US 
            FROM YP_AQI 
            WHERE AQI_US = (SELECT MAX(AQI_US) FROM YP_AQI);
        """
        )
        result = cs.fetchone()
        DATE, AQI_US = result
        return AQIUsValues(date=DATE, aqi_us=AQI_US)


@app.get("/api/aqi/min/pm25")
async def get_min_pm25() -> PM25Values:
    """Return the minimum PM2.5 of the whole dataset included Air Quality Index."""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT 
            TS, 
            PM25 
            FROM YP_AQI 
            WHERE PM25 = (SELECT MIN(PM25) FROM YP_AQI);
        """
        )
        result = cs.fetchone()
        DATE, PM25 = result
        return PM25Values(date=DATE, pm25=PM25)


@app.get("/api/aqi/max/pm25")
async def get_max_pm25() -> PM25Values:
    """Return the maximum PM2.5 of the whole dataset included Air Quality Index."""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT 
            TS, 
            PM25
            FROM YP_AQI 
            WHERE PM25 = (SELECT MAX(PM25) FROM YP_AQI);
        """
        )
        result = cs.fetchone()
        DATE, PM25 = result
        return PM25Values(date=DATE, pm25=PM25)


@app.get("/api/noise/avg")
async def get_noise_aqi() -> NoiseValues:
    """Return the average noise level of the whole dataset included."""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT AVG(AVG) as AVG_NOISE
            FROM YP_NOISE;
        """
        )
        result = cs.fetchone()
        return NoiseValues(date=datetime.now(), dB=result[0])


@app.get("/api/noise/avg/daily")
async def get_daily_avg_noise() -> list[NoiseValues]:
    """Return average noise value of each day in decibel"""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT DATE(TS) as date,
            AVG(AVG) as dB
            FROM YP_NOISE
            GROUP BY date;
        """
        )
        result = [NoiseValues(date=DATE, dB=dB) for DATE, dB in cs.fetchall()]
    return result


@app.get("/api/noise/min")
async def get_min_noise() -> NoiseValues:
    """Return the minimum noise of the whole dataset."""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT 
            TS, 
            AVG 
            FROM YP_NOISE
            WHERE AVG = (SELECT MIN(AVG) FROM YP_NOISE);
        """
        )
        result = cs.fetchone()
        DATE, dB = result
        return NoiseValues(date=DATE, dB=dB)


@app.get("/api/noise/max")
async def get_max_noise() -> NoiseValues:
    """Return the maximum noise of the whole dataset."""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT 
            TS, 
            AVG 
            FROM YP_NOISE
            WHERE AVG = (SELECT MAX(AVG) FROM YP_NOISE);
        """
        )
        result = cs.fetchone()
        DATE, dB = result
        return NoiseValues(date=DATE, dB=dB)


@app.get("/api/noise/day/{day_id}")
async def get_day_noise(day_id: int) -> list[NoiseValues]:
    """Return selected day noise value included noise in dB."""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT TS,
            AVG
            FROM YP_NOISE
            WHERE DAYOFWEEK(TS)=%s
        """,
            [day_id],
        )
        result = [NoiseValues(date=DATE, dB=AVG) for DATE, AVG in cs.fetchall()]
        if not result:
            raise HTTPException(status_code=404, detail="[Noise] Data not found")
    return result


@app.get("/api/traffic/avg")
async def get_avg_traffic() -> list[TrafficValues]:
    """Return the average traffic values (high flow/ no traffic) of all datasets"""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
        SELECT sector, 
            AVG(currSpeed), 
            AVG(freeFlowSpeed), 
            SUM(roadClosure)
            FROM YP_TRAFFIC
            GROUP BY sector;
        """
        )
        result = [
            TrafficValues(
                date=datetime.now(),
                sector=sector,
                curr_speed=currSpeed,
                freeflow_speed=freeFlowSpeed,
                road_closure=roadClosure,
            )
            for sector, currSpeed, freeFlowSpeed, roadClosure in cs.fetchall()
        ]
        return result


@app.get("/api/traffic/avg/daily")
async def get_daily_avg_traffic() -> list[TrafficValues]:
    """Return average daily traffic"""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT DATE(TS) as date, 
            sector, 
            AVG(currSpeed), 
            AVG(freeFlowSpeed), 
            SUM(roadClosure)
            FROM YP_TRAFFIC
            GROUP BY date, sector
        """
        )
        result = [
            TrafficValues(
                date=DATE,
                sector=sector,
                curr_speed=currSpeed,
                freeflow_speed=freeFlowSpeed,
                road_closure=roadClosure,
            )
            for DATE, sector, currSpeed, freeFlowSpeed, roadClosure in cs.fetchall()
        ]
    return result


@app.get("/api/traffic/day/{day_id}")
async def get_day_traffic(day_id: int):
    """Return traffic values for a selected day"""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT TS as date, 
            sector, 
            AVG(currSpeed), 
            AVG(freeFlowSpeed), 
            SUM(roadClosure)
            FROM YP_TRAFFIC
            WHERE DAYOFWEEK(TS)=%s
            GROUP BY date, sector
        """,
            [day_id],
        )
        result = [
            TrafficValues(
                date=DATE,
                sector=sector,
                curr_speed=currSpeed,
                freeflow_speed=freeFlowSpeed,
                road_closure=roadClosure,
            )
            for DATE, sector, currSpeed, freeFlowSpeed, roadClosure in cs.fetchall()
        ]
        if not result:
            raise HTTPException(status_code=404, detail="[Traffic] Data not found")
    return result


@app.get("/api/traffic/road/{road_id}")
async def get_road_traffic(road_id: int):
    """Return traffic values of a given road"""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
            SELECT TS as date, 
            sector, 
            AVG(currSpeed), 
            AVG(freeFlowSpeed), 
            SUM(roadClosure)
            FROM YP_TRAFFIC
            WHERE sector=%s
            GROUP BY date, sector
        """,
            [road_id],
        )
        result = [
            TrafficValues(
                date=DATE,
                sector=sector,
                curr_speed=currSpeed,
                freeflow_speed=freeFlowSpeed,
                road_closure=roadClosure,
            )
            for DATE, sector, currSpeed, freeFlowSpeed, roadClosure in cs.fetchall()
        ]
        if not result:
            raise HTTPException(status_code=404, detail="[Traffic] Data not found")
    return result


@app.get("/api/traffic/min")
async def get_min_traffic() -> list[TrafficValues]:
    """Return the minimum traffic values (the most traffic) of all datasets"""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
        SELECT
        sector, 
        MIN(currSpeed), 
        MIN(freeFlowSpeed), 
        MIN(roadClosure)
        FROM YP_TRAFFIC
        GROUP BY sector;
        """
        )
        result = [
            TrafficValues(
                date=datetime.now(),
                sector=sector,
                curr_speed=currSpeed,
                freeflow_speed=freeFlowSpeed,
                road_closure=roadClosure,
            )
            for sector, currSpeed, freeFlowSpeed, roadClosure in cs.fetchall()
        ]
        return result


@app.get("/api/traffic/max")
async def get_max_traffic() -> list[TrafficValues]:
    """Return the maximum traffic values (the least traffic) of all datasets"""
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute(
            """
        SELECT
        sector, 
        MAX(currSpeed), 
        MAX(freeFlowSpeed), 
        MAX(roadClosure)
        FROM YP_TRAFFIC
        GROUP BY sector;
        """
        )
        result = [
            TrafficValues(
                date=datetime.now(),
                sector=sector,
                curr_speed=currSpeed,
                freeflow_speed=freeFlowSpeed,
                road_closure=roadClosure,
            )
            for sector, currSpeed, freeFlowSpeed, roadClosure in cs.fetchall()
        ]
        return result
