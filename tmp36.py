from gpiozero import LED
from gpiozero import MCP3008
from time import sleep
led1 = LED(12)
led2 = LED(5)
led3 = LED(6)
led4 = LED(13)
led5 = LED(19)
led6 = LED(26)


while True:
    temp = MCP3008(channel=0)
    waarde = temp.value * (3.3/1)
    uitkomst =(waarde - 0.5) * 100
    


    print(uitkomst)

    if uitkomst < 5:
        led1.on()
    else:
        led1.off()
    if uitkomst >= 5 and uitkomst < 10:
        led2.on()
    else:
        led2.off()
    if uitkomst >= 10 and uitkomst < 15:
        led3.on()
    else:
        led3.off()
    if uitkomst >=15 and uitkomst < 20:
        led4.on()
    else:
        led4.off()
    if uitkomst >=20 and uitkomst < 25:
        led5.on()
    else:
        led5.off()
    if uitkomst >=25:
        led6.on()
    else:
        led6.off()
    sleep(1)
