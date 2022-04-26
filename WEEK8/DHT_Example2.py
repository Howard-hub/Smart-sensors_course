from machine import Pin
import dht, time
import network
import urequests
sta=network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('NETGEAR71','silkypiano846')
while not sta.isconnected() :
    pass
print('Wifi連線成功')
p0=Pin(4, Pin.IN)
d=dht.DHT11(p0)
device_id = "29490513096"
headers={"CK":"DKYSCBR7ZXGA0STTU7"}
url_CHT="http://iot.cht.com.tw/iot/v1/device/"+device_id+"/rawdata"
d.measure()
t=d.temperature()
h=d.humidity()
CHT_data=[{"id":"DHT-TEMP","value":[str(t)]}]
urequests.post(url_CHT,json=CHT_data,headers=headers)
CHT_data=[{"id":"DHT-Hum","value":[str(h)]}]
urequests.post(url_CHT,json=CHT_data,headers=headers)
print("上傳完畢")
time.sleep(600)
machine.reset()