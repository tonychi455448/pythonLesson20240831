from machine import ADC
import time

while True:
    adc = machine.ADC(4) # Connect to GP26, which is channel 0
    temp1=adc.read_u16()/65535*3.3
    temp1= 27 - (temp1 - 0.706)/0.001721
    print(temp1)
    time.sleep(1)