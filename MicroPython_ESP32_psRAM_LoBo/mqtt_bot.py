import time
from machine import DHT
import urequests

class Btn1(Pin):  
  pass
  pass  
  
TOKEN = 'IX1RkhYoWtVnfpRKkxVHJKedPosV7hO/XYHsWRQ09ai0DV0YuBHN9SNOFFXijiU2IYlTNFJB/qkdx49RuztNbdr3JyLb4Q7duN48ulGeUrWN8rzj3g5aDeWg+baY4akHER3FKDAaa7mtVZQ2xvnM4AdB04t89/1O/w1cDnyilFU=' URL = 'https://api.line.me/v2/bot/message/push'  btn1 = Btn1(18, Pin.IN)btn2 = Btn2(19, Pin.IN)
d = DHT(Pin(17), DHT.DHT2X)
    if topic.decode('utf-8') == '/line/bot/temperature/get':    
      result , t, h = d.read()    
      print(result , t, h)    
    if result:      
      client.publish('/line/bot/temperature', json.dumps({'status': 1, 'temperature': '{0:.2f}'.format(t), 'humidity': '{0:.2f}'.format(h)}))
      client.publish('/line/bot/temperature', json.dumps({'status': 0, 'msg': 'invalid read temperature sensor'}))def _connect(): client.connect() client.subscribe('/line/bot/gpio') client.subscribe('/line/bot/goio/status/get') client.subscribe('/line/bot/goio/status/get/all')  client.subscribe('/line/bot/temperature/get')  
client.set_callback(sub_cb) 
_connect()
time.sleep(2)
print('Start main loop ...') 



th.start_new_thread('btn1', btn_handler, (btn1,))
th.start_new_thread('btn2', btn_handler, (btn2,))