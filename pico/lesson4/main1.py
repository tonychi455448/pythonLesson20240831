from machine import Pin
import time

led=Pin("LED",Pin.OUT)
status=False 
# i=0
while True:
    if status==False:
        status=True 
        led.on()
    else:
        status=False  
        led.off()
    time.sleep(1)
#     i+=1
#     led.value(i%2)
#     time.sleep(1)
#     print(i%2)
#led.on()    
