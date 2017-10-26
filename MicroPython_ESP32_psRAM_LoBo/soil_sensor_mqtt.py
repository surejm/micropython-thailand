import machine, ubinascii

timer1 = Timer(1)
power = ADC(Pin(33))
  
def read_data():
  global d 
  global CLIENT_ID
  global mqtt 
  topic = 'plant/{0}/temperature'.format(CLIENT_ID.decode("utf-8"))
  result , t, h = d.read() 
  if result:
    _tm = time.localtime()
    _strTime = '{0}/{1}/{2} {3}:{4}:{5}'.format(_tm[2], _tm[1], _tm[0], _tm[3] + 6, _tm[4], _tm[5])
    soil = {'id': 1, 'value': read_soil(1)}
    msg =  json.dumps({
        'Id': CLIENT_ID,                    
        'plant': _plant_no,
        'datetime': _strTime,
        'temperature': '{0:.2f}'.format(t), 
        'humidity': '{0:.2f}'.format(h),
        'soil': soil,
        'power': power.read()
    })
    print(topic, msg) 
    mqtt.publish(topic, msg)
  else:
    print('DHT Sensor read error') 
    
def subscb(task):
    print("[{}] Subscribed".format(task))
    
  global _plant_no
  global mqtt
  mqtt.subscribe('plant/{0}/temperature/get'.format(_plant_no))
  global _plant_no
  global mqtt
  
  if msg[1] == 'plant/{0}/temperature/get'.format(_plant_no):
    print(msg[1], msg)
    read_data()
                          clientid=CLIENT_ID, keepalive = 30, retain=1, qos=0,  
                          connected_cb=conncb, data_cb=datacb, subscribed_cb=subscb)
print('Wait mqtt connection...')
print('Start main task...')