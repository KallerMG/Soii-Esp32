import machine
adc = machine.ADC(machine.Pin(36))
print(adc.read())
   
