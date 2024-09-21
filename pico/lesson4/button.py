from machine import Pin
import time

led1=Pin(15,Pin.OUT)
button=Pin(14,Pin.IN,Pin.PULL_DOWN)

while True:
    if button.value():
        print(str(button.value()))
        led1.toggle()
        time.sleep(0.5)