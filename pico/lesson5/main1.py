from machine import ADC
import time

while True:
    adc = machine.ADC(4) # Connect to GP26, which is channel 0
    temp1=adc.read_u16()
    #temp1=temp1/65535
    print(temp1)
    time.sleep(1)