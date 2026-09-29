from gpiozero import LEDBarGraph 
from time import sleep 

graph = LEDBarGraph(17,27,22,10,11,20)

graph.value = 1 
sleep(1)
graph.value = 1/2
sleep(1)
graph.value = -1/2
sleep(1)
graph.value = 1/4
sleep(1)
graph.value = -1
sleep(1)