import sys
from Adafruit_IO import MQTTClient
import time
import random

class mqtt_client:
  AIO_FEED_IDs = ['nutnhan1', 'nutnhan2']
  AIO_USERNAME = 'nguyentruongthan'
  AIO_KEY = 'aio_MhKB20qftEDbOoRclChw5r4cKnzg'

  def __init__(self):
    self.client = MQTTClient(self.AIO_USERNAME, self.AIO_KEY)
    self.client.on_connect = self.connected
    self.client.on_disconnect = self.disconnected
    self.client.on_message = self.message
    self.client.on_subscribe = self.subscribe

    self.client.connect()
    self.client.loop_background()

  
  def connected(self, client, ):
    print('Connected successful ...')
    for topic in self.AIO_FEED_IDs:
      client.subscribe(topic)

  def subscribe(self, client, userdata, mid, granted_qos):
    print('Subscribe successful ...')

  def disconnected(self, client):
    print('Disconnect ...')
    sys.exit(1)

  def message(self, client, feed_id, payload):
    print(f'Receive data: {payload}, feed id: {feed_id}')

  def publish(self, feed_id, message):
    self.client.publish(feed_id, message)

if __name__ == '__main__':  
  
  mqtt = mqtt_client()

  count = 10
  object_publish = 0
  number_of_sensor = 3
  while 1:
    #send random data of three sensors to server every 30s
    count -= 1
    if(count <= 0):
      count = 10
      if(object_publish == 0):
        #send data to Temperature Sensor (cambien1)
        temp = random.randint(10, 20)
        print(f'Publishing data = {temp} degC to Temperature Sensor (cambien1)')  
        mqtt.publish('cambien1', temp)
      elif(object_publish == 1):
        #send data to Light Sensor (cambien2)
        light = random.randint(100, 500)
        mqtt.publish('cambien2', light)
        print(f'Publishing data = {light} lux to Light Sensor (cambien2)')  
      elif(object_publish == 2):
        #send data to Humidity Sensor (cambien3)
        humi = random.randint(50, 70)
        mqtt.publish('cambien3', humi)
        print(f'Publishing data = {humi} % to Humidity Sensor (cambien3)')  

      #updata sensor which will publish in next time 
      object_publish = (object_publish + 1) % 3

    time.sleep(1)
