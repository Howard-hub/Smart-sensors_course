'''
IOT_ADC_Test 功能2
將可變電阻的浮動腳接到A0、將S2接到GOIO16、將S3接到GOIO5、
LED3接到GPIO14
    • ADC副程式：進行A0上的電壓偵測，並將該電壓轉換為PWM的Duty Cycle輸出到GPIO14上的LED2，藉此改變LED的亮度。電壓越高，亮度越低。
    • 功能1：當奇數次按下S2時開始ADC程式，當偶數次按下S2時關閉ADC程式
    • 功能2：當按下S3時，在Shell上顯示End Program!並關閉整個程式
'''
from machine import Pin, PWM, ADC
import time

ledPin = Pin(14, Pin.OUT)
LED = PWM(ledPin,1000)

SW1=Pin(16,Pin.IN)
SW2=Pin(5,Pin.IN,Pin.PULL_UP)

def adc():
    while True:
        adc = ADC(0)
        val = adc.read()
        LED.duty(1024-val)
        print('POT: ', str(val))
        time.sleep(0.5)
        if(SW1.value()==0):
            break
while True:
    if(SW1.value()==0):
        adc()
        while (SW1.value()==0):
            pass
    elif(SW2.value()==0):
        print("End Program!")
        break