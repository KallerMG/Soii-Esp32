import network
def conectar():
  station = network.WLAN(network.STA_IF)
  station.active(True)
  if not station.isconnected():
    station.connect("ssid", "senha")
    return (void)
