#!/usr/bin/env python3
import ambient
import sys
import time
import datetime
import schedule

from sensor.grove_tds import GroveTDS
from sensor.grove_temperature_humidity_sensor import DHT

DHT_TYPE = "11"
DHT_PIN = 12
TDS_CHANNEL = 0
AMBIENT_CHANNEL_ID = "-----"
AMBIENT_WRITE_KEY = "----------------"


def get_sensor_info():
    humi, temp = dht_sensor.read()

    data = {
        "created": datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S"),
        "d1": temp,
        "d2": humi,
        "d3": round(tds_sensor.TDS, 2)
    }
    am.send(data)


def main():
    schedule.every(1).minutes.do(get_sensor_info)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    dht_sensor = DHT(DHT_TYPE, DHT_PIN)
    tds_sensor = GroveTDS(TDS_CHANNEL)
    am = ambient.Ambient(AMBIENT_CHANNEL_ID, AMBIENT_WRITE_KEY)
    main()
