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
    #print("start")
    f=open('DHT_Temp.txt','a+')
    while True:
        
        Temperature=0
        Humidity=0
        landHumidity=0
        val = adc.read()

        d.measure()
        t=d.temperature()
        h=d.humidity()
        Temperature=t
        Humidity=h
        landHumidity=val/10.24
        

        #Buzzer.duty(1024)
        LED2.value(0)
        if(landHumidity>50):
            Buzzer.duty(0)
            LED2.value(0)
            print("Warning! Soil moisture too HIGH! Current moisture is "+ str(landHumidity) +"%")
            f.write("Warning! Soil moisture too HIGH! Current moisture is "+ str(landHumidity) +"%"+"\n")
            LED2.value(1)
            time.sleep(0.5)
            LED2.value(0)           
        elif(landHumidity<30):
            Buzzer.duty(0)
            LED2.value(0)
            print("Warning! Soil moisture too LOW! Current moisture is "+ str(landHumidity) +"%")
            f.write("Warning! Soil moisture too LOW! Current moisture is "+ str(landHumidity) +"%"+"\n")
            Buzzer.duty(900)
            time.sleep(0.5)
            LED2.value(1)
            Buzzer.duty(0)
            time.sleep(0.5)
        else:
            Buzzer.duty(1024)
        
            
        payload=[{"id":"DHT-TEMP","value":[Temperature]}]
        client.publish( b'/v1/device/29490513096/rawdata',str(payload).encode() )
        
        payload=[{"id":"DHT-Hum","value":[Humidity]}]
        client.publish(b'/v1/device/29490513096/rawdata',str(payload).encode())
        
        payload=[{"id":"land-humidity","value":[landHumidity]}]
        client.publish(b'/v1/device/29490513096/rawdata',str(payload).encode())
        
        j=j+1
        print('第'+str(j)+'筆'+'publish finish')
        
        time.sleep(3)
        break
    f.close()
    client.disconnect()