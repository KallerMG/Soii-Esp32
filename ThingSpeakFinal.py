import wifi
import temp
import time
from umqtt.simple import MQTTClient
exec(open('./temp.py').read(),globals())
exec(open('./wifi.py').read(),globals())
conectar()
servidor = "mqtt.thingspeak.com"
client = MQTTClient("umqtt_client", servidor)
idCanal = "idcanal"
ApiKey = "api key"
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
