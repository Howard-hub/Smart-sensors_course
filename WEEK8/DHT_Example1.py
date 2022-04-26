from machine import Pin
import dht 
import time
p0=Pin(4, Pin.IN)
d=dht.DHT11(p0) #建立 DHT11 物件
while True:
    d.measure() #重新測量溫溼度
    t=d.temperature() #讀取攝氏溫度
    h=d.humidity() #讀取相對溼度
    print('Temperature=', t, 'C', 'Humidity=', h, '%')
    time.sleep(2) #暫停 2 秒