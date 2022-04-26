from machine import Pin
import time
LED=Pin(14,Pin.OUT)
SW1=Pin(16,Pin.IN)
SW2=Pin(5,Pin.IN,Pin.PULL_UP)
while 1:
    if(SW1.value()==0 and SW2.value()==0):
        print("All pressed")
        time.sleep(1)
    elif(SW1.value()==0 and SW2.value()==1):
        print("sw1 pressed")
        LED.value(not LED.value())
        time.sleep(0.5)
    elif(SW1.value()==1 and SW2.value()==0):
        print("sw2 presses")
        time.sleep(1)
    elif(SW1.value()==1 and SW2.value()==1):
        LED.value(not LED.value())
        time.sleep(3)