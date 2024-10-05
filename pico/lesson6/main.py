#! usr/bin/micropython
'''
led->gpio15
光敏電阻->gpio28
可變電阻->gpio26
內建溫度sensor->adc(4) adc最後1pin，共5pin
'''
import time,binascii
from umqtt.simple import  MQTTClient
import tools
from machine import Timer,ADC,Pin,PWM,RTC
def do_thing(t):
    '''
    :param t:Timer的實體 
    處理溫度和光線
    每2秒執行1次
    '''
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(f'溫度:{temperature}')
    mqtt.publish("SA-58/Temperature",f"{temperature}")
    light_value = adc_light.read_u16()
    print(f'光線:{light_value}')
    mqtt.publish("SA-58/Light",f"{light_value}")
    
    
def do_thing1(t):
    '''
    :param t:Timer的實體 
    處理可變電阻
    每1秒執行1次
    '''
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)    
    print(f'可變電阻:{round(duty/65535*10)}')
    mqtt.publish("SA-58/switch",f"{round(duty/65535*10)}")
    
def main():
    t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
    t2 = Timer(period=1000, mode=Timer.PERIODIC, callback=do_thing1)
    
if __name__ == "__main__":
    #pico_連結電腦時的寫法,要用connect
    try:
        tools.connect()
        pass
    except RuntimeError as e:
        print(f"{{e}")
    except Exception:
        print("未知錯誤")
    else:
        #sensor setup
        adc = ADC(4) #內建溫度感測器
        adc_light = ADC(Pin(28)) #光線感測器
        pwm = PWM(Pin(15),freq=50) #可變電阻
        conversion_factor = 3.3 / (65535) #電壓轉換率
        SERVER="192.168.0.252"
        CLIENT_ID=binascii.hexlify(machine.unique_id())
        mqtt=MQTTClient(CLIENT_ID,SERVER,user="pi",password="raspberry")
        mqtt.connect()
        main()