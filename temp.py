def temperatura(): #LM35 valor aproximado
  import machine
  adc = machine.ADC(machine.Pin(36))
  temp = adc.read()
  return (temp*(3.3/1024)*10)
