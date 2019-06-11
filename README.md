# Bem vindo a wiki do kaller ESP-32!
### Plataforma utilizada para o desenvolvimento (ESP-32).
<img src="https://www.curtocircuito.com.br/pub/media/catalog/product/cache/ecd051e9670bd57df35c8f0b122d8aea/p/l/placa_doit_esp32_-_esp-wroom-32_-_wifi_bluetooth.jpg" width="100" height="100" />
<img src="https://www.curtocircuito.com.br/pub/media/catalog/product/cache/ecd051e9670bd57df35c8f0b122d8aea/p/l/placa_doit_esp32_-_esp-wroom-32_-_wifi_bluetooth.jpg" width="200" height="200" />
<img src="https://www.curtocircuito.com.br/pub/media/catalog/product/cache/ecd051e9670bd57df35c8f0b122d8aea/p/l/placa_doit_esp32_-_esp-wroom-32_-_wifi_bluetooth.jpg" width="300" height="300" />
### * Sensor de temperatura LM35.
<img src="https://5.imimg.com/data5/VU/WA/MY-45609829/lm35-temperature-sensor-500x500.png" width="100" height="100" />
<img src=https://5.imimg.com/data5/VU/WA/MY-45609829/lm35-temperature-sensor-500x500.png" width="200" height="200" />
<img src="https://5.imimg.com/data5/VU/WA/MY-45609829/lm35-temperature-sensor-500x500.png" width="300" height="300" />

## Trabalho sistemas operacionais II
   Começando a desenvolver uma plataforma que se comunica com a nuvem (ThingSpeak) por WIFI, proporcionando uma melhor visualização do conteúdo lido pelos sensores por meio de gráficos e tabelas e tem uma capacidade de reação e poder de processamento, podendo ir muito além.
* Link para ThingSpeak: https://thingspeak.com/
* Link para tutorial de comunicação com a plataforma: https://mjrobot.org/2018/06/13/iot-feito-facil-esp-micropython-mqtt-thingspeak/
* Link sobre como instalar o MicroPython: https://www.dobitaobyte.com.br/como-instalar-o-firmware-micropython-no-esp32/
* Site do MicroPython: https://micropython.org/ 

## Protocolo MQTT
   É um protocolo de mensagens leve para sensores e pequenos dispositivos móveis otimizado para redes TCP/IP não confiáveis ou de alta latência, O esquema de troca de mensagens é fundamentado no modelo Publicador-Subscritor.
   * O protocolo leve permite a implementação em hardware de dispositivo altamente restringido e em redes de largura da banda limitada e de alta latência.
   * Sua flexibilidade possibilita o suporte a diversos cenários de aplicativo para dispositivos e serviços de IoT.
   ![](https://www.electronicwings.com/public/images/user_images/images/NodeMCU/NodeMCU%20Basics%20using%20ESPlorer%20IDE/NodeMCU%20MQTT%20Client/MQTT%20Broker%20nw.png)
 ### Exemplo de código para publicar:
```from umqtt.simple import MQTTClient

def main(server="servidor"):#servidor para publicar
    c = MQTTClient("umqtt_cliente", server) #iniciando cliente
    c.connect() #conectando
    c.publish(b"ola_topico", b"ola mundo") #publicando
    c.disconnect() #desconectando

if __name__ == "__main__":
    main()
```




### ThingSpeak
  O ThingSpeak ™ é um serviço de plataforma de analítica da IoT que permite agregar, visualizar e analisar fluxos de dados ao vivo na nuvem. O ThingSpeak fornece visualizações instantâneas de dados postados por seus dispositivos no ThingSpeak. Com a capacidade de executar o código MATLAB® no ThingSpeak, você pode realizar a análise e o processamento on-line dos dados conforme eles são recebidos. O ThingSpeak é frequentemente usado para prototipagem e sistemas IoT de verificação de conceito que exigem análise.
  * Configure facilmente dispositivos para enviar dados para o ThingSpeak usando protocolos IoT populares.
  * Visualize seus dados do sensor em tempo real.
  * Agregar dados sob demanda de fontes de terceiros.
  * Use o poder do MATLAB para entender seus dados de IoT.
  * Execute sua análise da IoT automaticamente com base em agendamentos ou eventos.
  * Prototipar e construir sistemas de IoT sem configurar servidores ou desenvolver software da web.
### Exemplos de formas para visualizar o conteudo:
![](https://hackster.imgix.net/uploads/attachments/417896/screen_shot_2018-02-06_at_1_49_32_pm_BnPtYdUS9G.png?auto=compress%2Cformat&w=900&h=675&fit=min)








