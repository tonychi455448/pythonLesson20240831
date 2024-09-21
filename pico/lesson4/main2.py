from machine import Timer,Pin

#tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
#tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))

green_led=Pin("LED",Pin.OUT)
green_led.off()

red_led=Pin(15,Pin.OUT)
red_led.off()

#button = Pin(14, Pin.IN, Pin.PULL_DOWN)

green_count=0
red_count=0
def green_run1(t:Timer):
    global green_count
    green_count+=1
    print(f"綠燈執行 {green_count} 次")
    green_led.toggle()
    if green_count >=10:
        t.deinit()
        green_led.off()
    pass

def red_run2(t:Timer):
    global red_count
    red_count+=1
    print(f"紅燈執行 {red_count} 次")
    red_led.toggle()
    if red_count >=5:
        t.deinit()
        red_led.off()
    pass

led_timer=Timer(period=1000,mode=Timer.PERIODIC,callback=green_run1)
led_timer2=Timer(period=2000,mode=Timer.PERIODIC,callback=red_run2)

