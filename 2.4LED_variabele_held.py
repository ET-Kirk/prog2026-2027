from gpiozero import PWMLED
from time import sleep

Led = PWMLED(17)

while True:
    Led.value = 0 
    sleep(1)
    Led.value = 0.5
    sleep(1)
    Led.value = 1 
    sleep(1)