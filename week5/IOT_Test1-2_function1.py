from machine import Pin
import time
SW1=Pin(16,Pin.IN)
SW2=Pin(5,Pin.IN,Pin.PULL_UP)
LED=Pin(14,Pin.OUT)

def ReadKey():
    temp=0
    if(SW1.value()==0):
        temp = temp + 2
    if(SW2.value()==0):
        temp = temp + 1
    return temp
while 1:
    if (ReadKey()==3):
        print("all pressed")
        while((ReadKey()==3)):
            pass
    elif(ReadKey()==2):
        print("SW1 pressed")
        while((ReadKey()==2)):
            LED.value(1)
            time.sleep(0.3)
            LED.value(0)
            time.sleep(0.3)
    elif(ReadKey()==1):
        print("SW2 presses")
        while((ReadKey()==1)):
            pass
    else:
        LED.value(1)
        time.sleep(1.5)
        LED.value(0)
        time.sleep(1.5)
    