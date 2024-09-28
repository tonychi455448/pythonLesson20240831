from machine import ADC,Timer,Pin,PWM,RTC

#Define Pin
adc1 = machine.ADC(4) # Connect to GP26, which is channel 0
adc2 = machine.ADC(Pin(26))
pwm = PWM(Pin(15),freq=1000)
buttonY=Pin(14, Pin.IN)
greenLED=Pin("LED", Pin.OUT)
#redLED=Pin(15, Pin.OUT)

#Initial
greenLED.off()
switchState=False 
#redLED.off()

def readTemp(t):
    temp1=adc1.read_u16()/65535*3.3
    temp1= 27 - (temp1 - 0.706)/0.001721
    temp1=round(temp1,2)
    print(f"內建溫度:{temp1}度")

def blinkGreenLED(t):
    greenLED.toggle()
'''
def switchRedLED(t):
    if buttonY.value():
        print("press")
        redLED.toggle()
'''
def readADC(t):
    global switchState
    if buttonY.value():
        switchState=not switchState
        
    if switchState==True :
        duty = adc2.read_u16() 
    else:
        duty=0
    pwm.duty_u16(duty)

def readTime(t):
    year, month, day, weekday, hours, minutes, seconds, subseconds= RTC().datetime()
    print(f"{hours}:{minutes}:{seconds}")

tim = Timer(period=5000, mode=Timer.PERIODIC, callback=readTemp)
tim2 = Timer(period=500, mode=Timer.PERIODIC, callback=blinkGreenLED)
#tim3 = Timer(period=500, mode=Timer.PERIODIC, callback=switchRedLED)
tim4 = Timer(period=100, mode=Timer.PERIODIC, callback=readADC)
tim5 = Timer(period=1000, mode=Timer.PERIODIC, callback=readTime)