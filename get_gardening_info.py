import sys
import time

from sensor.grove_tds import GroveTDS
from sensor.grove_temperature_humidity_sensor import DHT

DHT_TYPE = "11"
DHT_PIN = 12
TDS_CHANNEL = 0

def main():
    dht_sensor = DHT(DHT_TYPE, DHT_PIN)
    tds_sensor = GroveTDS(TDS_CHANNEL)

    while True:
        humi, temp = dht_sensor.read()
        print('TDS Value: {0}'.format(tds_sensor.TDS))
        if not humi is None:
            print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(dht_sensor.dht_type, humi, temp))
        else:
            print('DHT{0}, humidity & temperature: {1}'.format(dht_sensor.dht_type, temp))
        time.sleep(1)


if __name__ == '__main__':
    main()