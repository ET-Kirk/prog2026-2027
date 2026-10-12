import time 
import board 
import adafruit_dht
from gpiozero import MCP3008
dhtDevice = adafruit_dht.DHT11(board.D18)
volgteller = 0
verschil_temp = 0
f = open("tempdata.txt","w")
while True:
    volgteller = volgteller +1 
    temp = MCP3008(channel=0)
    waarde = temp.value * (3.3/1)
    uitkomst =(waarde - 0.5) * 100
    try:
        temperature_dht = dhtDevice.temperature
        gem = (uitkomst + temperature_dht) /2
        verschil_temp = uitkomst - temperature_dht
        if verschil_temp < 0:
            verschil_temp = -verschil_temp
        f = open("tempdata.txt","a")
        f.write(f" regel {volgteller} ")
        f.write(f" temperatuur DHT {temperature_dht:.1f} en temperatuur {uitkomst} , gem = {gem} , verschil = {verschil_temp} /")
        f.close()
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(3.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
    time.sleep(3.0)