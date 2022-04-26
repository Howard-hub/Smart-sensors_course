from machine import Pin,ADC
import dht
import time
import network 
from umqtt.robust import MQTTClient
sta=network.WLAN(network.STA_IF)
sta.active(True) 
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
    f=open('DHT_Temp.txt','w')
    while True:
        Temperature=0
        Humidity=0
        # 執行5次之後才上傳一次資料
        for i in range(5):
            d.measure()
            t=d.temperature()
            h=d.humidity()
            Temperature=Temperature+t
            Humidity=Humidity+h
            time.sleep(2)
            
        Temperature=int(Temperature/5)
        Humidity=int(Humidity/5)
        
        payload=[{"id":"DHT-TEMP","value":[Temperature]}]
        client.publish( b'/v1/device/29490513096/rawdata',str(payload).encode() )
        
        payload=[{"id":"DHT-Hum","value":[Humidity]}]
        client.publish(b'/v1/device/29490513096/rawdata',str(payload).encode())
        
        j=j+1
        print('第'+str(j)+'筆'+'publish finish')
        f.write(str(Temperature)+' '+str(Humidity)+'\n')
        time.sleep(5)
        break
    f.close()
    client.disconnect()
