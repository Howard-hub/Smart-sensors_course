from machine import Pin,ADC,PWM
import dht
import time
import network 
from umqtt.robust import MQTTClient

S1=Pin(16,Pin.IN)
LED1=Pin(14,Pin.OUT)
LED2=Pin(12,Pin.OUT)
adc = ADC(0)
Buzzer = PWM(LED1,1000)

sta=network.WLAN(network.STA_IF)
sta.active(True) 
#sta.connect('NETGEAR71','silkypiano846')
sta.connect('CliffKuo_4G','cliff6005') 
while not sta.isconnected() :
    pass
print('Wifi連線成功')
p0=Pin(4, Pin.IN)
d=dht.DHT11(p0)

mqtt_client_id = 'D1 mini-DHT11' 
CHT_URL = 'iot.cht.com.tw' 
CHT_USERNAME = "DKYSCBR7ZXGA0STTU7" 
CHT_IO_KEY = 'DKYSCBR7ZXGA0STTU7'

client = MQTTClient(client_id=mqtt_client_id,
                    server=CHT_URL,
                    user=CHT_USERNAME,
                    password=CHT_IO_KEY) 
j=0
while True:
    client.connect() #連線至MQTT伺服器
    f=open('DHT_Temp.txt','a+')
    while True:
        
        Temperature=0
        Humidity=0
        water_leavel=0
        emergency_switch=0
        val = adc.read()

        d.measure()
        t=d.temperature()
        h=d.humidity()
        Temperature=t
        Humidity=h
        water_leavel=val/10.24
        

        #Buzzer.duty(1024)
        LED2.value(0)
        if(water_leavel>45):
            Buzzer.duty(1024)
            LED2.value(0)        
        elif(water_leavel<45):
            if(S1.value()==0):
                emergency_switch=1
                print("emer")
            elif(emergency_switch==0):
                print("Warning! Water level too LOW! Current Level is "+ str(water_leavel) +"%")
                f.write("Warning! Water level too LOW! Current Level is "+ str(water_leavel) +"%"+"\n")
                Buzzer.duty(900)
                LED2.value(0)
                time.sleep(0.5)
                Buzzer.duty(0)
                LED2.value(1)
                time.sleep(0.5)
        
#         print(emergency_switch)
        payload=[{"id":"DHT-TEMP","value":[Temperature]}]
        client.publish( b'/v1/device/29490513096/rawdata',str(payload).encode() )
        
        payload=[{"id":"DHT-Hum","value":[Humidity]}]
        client.publish(b'/v1/device/29490513096/rawdata',str(payload).encode())
        
        payload=[{"id":"water_leavel","value":[water_leavel]}]
        client.publish(b'/v1/device/29490513096/rawdata',str(payload).encode())
        
        payload=[{"id":"emergency_switch","value":[emergency_switch]}]
        client.publish(b'/v1/device/29490513096/rawdata',str(payload).encode())
        
        j=j+1
        print('第'+str(j)+'筆'+'publish finish')
        
        time.sleep(3)
        break
    f.close()
    client.disconnect()
