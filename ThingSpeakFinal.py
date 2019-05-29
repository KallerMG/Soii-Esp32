import wifi
import temp
import time
from umqtt.simple import MQTTClient
print (conectar())
servidor = "mqtt.thingspeak.com"
client = MQTTClient("umqtt_client", servidor)
idCanal = "id do canal"
ApiKey = "api key do ThingSpeak"
topico = "channels/" + idCanal + "/publish/" + ApiKey
a = 1
while a == 1:
  temp = temperatura()
  print (temp)
  dados =  "field1="+str(temp)
  client.connect()
  client.publish(topico, dados)
  client.disconnect()
  time.sleep(30)  

