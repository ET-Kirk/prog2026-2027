import time 
import board 
import adafruit_dht
from w1thermsensor import W1ThermSensor , Unit
from gpiozero import LED
dhtDevice = adafruit_dht.DHT11(board.D18)
sensor = W1ThermSensor()
verschil_temp = 0
green = LED(16)
red = LED(20)
yellow = LED(21)
volgteller = 0
while True:
    temperature_in_celsius = sensor.get_temperature()
    volgteller = volgteller + 1
    try:
        temperature_c = dhtDevice.temperature
        verschil_temp = temperature_in_celsius - temperature_c
        if verschil_temp < 0:
            verschil_temp = -verschil_temp
        print(f"regel {volgteller}  Temp_DHT: {temperature_c:.1f} C en temp_BS18D20: {temperature_in_celsius}")
        if verschil_temp <= 1 :
            green.on()
            red.off()
            yellow.off()
            print("led groen brandt")
        elif verschil_temp < 5 and verschil_temp > 1 :
            green.off()
            red.off()
            yellow.on()
            print("led geel brandt")
        else:
            green.off()
            red.on()
            yellow.off()
            print("led rood brandt")

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(2.0)


