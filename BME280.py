import time 
import board
from adafruit_bme280 import basic as adafruit_bme280


i2c =board.I2C()

bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

bme280.sea_level_pressure = 1026

while True:
    print(f"\nTemp: {bme280.temperature:0.1f}°C")
    print(f"Druk: {bme280.pressure:0.1f} hPa")
    print(f"Vocht: {bme280.relative_humidity:0.1f} %")
    print(f"altitude = {bme280.altitude:0.2f} meters")
    time.sleep(2)
