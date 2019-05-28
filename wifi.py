import network
WiFi_SSID = "#erro404#"
WiFi_PASS = "NET10net@"
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WiFi_SSID, WiFi_SSID)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
