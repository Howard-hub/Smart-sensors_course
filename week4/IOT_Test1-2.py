from machine import Pin
LED=Pin(14,Pin.OUT)
SW1=Pin(16,Pin.IN)
SW2=Pin(5,Pin.IN,Pin.PULL_UP)
while 1:
    if(SW1.value()==0):
        print("End Progarm")
        break
    elif(SW2.value()==0):
        LED.value(not LED.value())