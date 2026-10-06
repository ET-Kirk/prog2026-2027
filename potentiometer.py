from gpiozero import LED
from gpiozero import MCP3008
from time import sleep
led = LED(21)
while True:
    potentiometer = MCP3008(channel=0)
    print(potentiometer.value)
    led.on()
    sleep(potentiometer.value)
    led.off()
    sleep(potentiometer.value)