# Program to read flow sensor and display flow rate in Serial Monitor.
# Source: Electrocredible.com, Language: MicroPython
from machine import Pin
import time

flow_frequency=0
flow_rate=0
lastcallTime=0

pin = Pin(21,Pin.IN,Pin.PULL_UP)
def callback(pin):
    global flow_frequency
    flow_frequency=flow_frequency+1
pin.irq(trigger=Pin.IRQ_RISING, handler=callback)
    
while True:
    if ((time.ticks_ms()-lastcallTime) > 1000):  #if time interval is more a than 1 second
        flow_rate = (flow_frequency * 60 / 7.5)  #flowrate in L/hour= (Pulse frequency x 60 min) / 7.5 
        flow_frequency = 0                       # Reset Counter
        lastcallTime=time.ticks_ms()
        print("Flow Rate={} Litres/Hour".format(flow_rate))   #print(flow_rate)
