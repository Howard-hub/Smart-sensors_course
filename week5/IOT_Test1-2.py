from machine import Pin
import time
S2=Pin(16,Pin.IN)
S3=Pin(5,Pin.IN,Pin.PULL_UP)
LED3=Pin(14,Pin.OUT)
while 1:
    if(S2.value()==0):
        print("END Shell")
        break
    elif(S3.value()==0):
        for i in range (7):
            LED3.value(1)
            time.sleep(3)
            LED3.value(0)
            time,sleep(1)