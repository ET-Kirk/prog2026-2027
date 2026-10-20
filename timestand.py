from time import sleep
import time as time
import board
from adafruit_bme280 import basic as adafruit_bme280
i2c =board.I2C()

bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
f = open("timedata.csv","w")
f.write(f"time                    , temp, pres  , altitude")
bme280.sea_level_pressure = 1026
while True:
    try:
        timestamp = time.ctime()
        f = open("timedata.csv","a")
        f.write(f"\n{timestamp}, {bme280.temperature:0.1f}, {bme280.pressure:0.1f}, {bme280.altitude:0.2f}")
        f.close()
    except RuntimeError as error:
        print(error.args[0])
        sleep(5)
        continue
    except Exception as error:
        adafruit_bme280.error
        raise error
    time.sleep(5)