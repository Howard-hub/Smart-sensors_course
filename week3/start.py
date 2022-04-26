from machine import Pin
import time
LED=Pin(2,Pin.OUT)
LED.value(1)
sleep(1000)
LED.value(0)