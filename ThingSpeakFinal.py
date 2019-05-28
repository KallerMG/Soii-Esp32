import network
import wifi
import temp
from umqtt.simple import MQTTClient
print (conectar())
servidor = "mqtt.thingspeak.com"
client = MQTTClient("umqtt_client", servidor)
idCanal = "789117"
ApiKey = "6WS8SD0T6DVHVA7D"
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

