from machine import ADC, Pin
import utime

def water_level_measurements():
    water_level = ADC(Pin(28)) # pin for analog values
    while True:
        print("Water Value is ---> %d" % water_level.read_u16())
        utime.sleep(1)
        
water_level_measurements()
