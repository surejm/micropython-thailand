from machine import I2C, Pin
from umqtt import MQTTClient 
import wifi_connect as wlan
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
client = None
oled.text('MicroPython', 10, 20)
oled.text('Waiting...', 10, 35)
oled.show()
wlan.connect()
oled.text('{0}'.format(wlan.get_ip()), 10, 50)
oled.show()
# MQTTClient
time.sleep(3)
def on_message(topic, msg):
  print(topic, msg)

client = MQTTClient(CLIENT_ID, '103.13.228.61')
client.set_callback(on_message)
client.connect()
client.subscribe('wifi/kit/temperature')
gc.collect()
  topic = 'micro/{0}/temperature'.format(CLIENT_ID.decode("utf-8"))
      msg =  json.dumps({
                'light': '{0:.0f}'.format(l.getLightIntensity()),
                'Id': CLIENT_ID, 
                'temperature': '{0:.2f}'.format(dht.temperature()), 
                'humidity': '{0:.2f}'.format(dht.humidity())
      })  
      client.publish(topic, msg)