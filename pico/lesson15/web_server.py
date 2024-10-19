import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
from machine import Timer,ADC,Pin,PWM,RTC
import machine

ssid = 'A590301'
password = 'A590301AA'

def getTemperature():
    '''
    處理溫度
    '''
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    temperature=round(temperature,1)
    print(f'溫度:{temperature}')
    return temperature

def getLightLevel():
    '''
    處理光線
    '''
    light_value = adc_light.read_u16()
    light_level = round(light_value/65535*10)
    print(f'光線:{light_value}')
    print(f'光線:{light_level}')
    if light_level>1:
        return "on"
    else:
        return "off"
    
def getSwitchLevel():
    '''
    處理可變電阻
    '''
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    switchLevel=round(duty/65535*10)
    print(f'可變電阻:{switchLevel}')
    return switchLevel

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage(temperature, state,temperature2,lightlevel,switchlevel):
    html = f"""
        <!DOCTYPE html>
        <html>
        <body>
        <form action="./lighton">
        <input type="submit" value="Light on" />
        </form>
        <form action="./lightoff">
        <input type="submit" value="Light off" />
        </form>
    
        <p>LED is {state}</p>
        <p>Temperature is {temperature}</p>
        <p>Temperature2 is {temperature}</p>
        <p>light is {lightlevel}</p>
        <p>switchlevel is {switchlevel}</p>
        
        <script>
            function fetchData() {{
                fetch('/data')
                    .then(response => response.text())
                    .then(data => {{
                        document.getElementById('data-container').innerHTML = data;
                    }});
            }}
            setInterval(fetchData, 1000); // 每5秒更新一次
            fetchData(); // 頁面加載時立即獲取數據
        </script>
    
        </body>
        </html>
    """
    return str(html)

def server(connection):
    #Start a web server
    state = 'OFF'
    pico_led.off()
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            pico_led.on()
            state = 'ON'
        elif request == '/lightoff?':
            pico_led.off()
            state = 'OFF'
            
        temperature = pico_temp_sensor.temp
        temperature2=getTemperature()
        lightlevel=getLightLevel()
        switchLevel=getSwitchLevel()
        
        html = webpage(temperature, state,temperature2,lightlevel,switchLevel)
        client.send(html)
        client.close()
        

if __name__ == "__main__":
    #sensor setup
    adc = ADC(4) #內建溫度感測器
    adc_light = ADC(Pin(28)) #光線感測器
    pwm = PWM(Pin(15),freq=50) #可變電阻
    conversion_factor = 3.3 / (65535) #電壓轉換率
    
    try:
        ip = connect()
        connection = open_socket(ip)
        server(connection)
    except KeyboardInterrupt:
        machine.reset()
    

