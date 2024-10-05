import time,binascii,machine,tools
from umqtt.simple import  MQTTClient

def main():
    try:
        tools.connect()
        mqtt=MQTTClient(CLIENT_ID,SERVER,user="pi",password="raspberry")
        mqtt.connect()
        while True :
            mqtt.publish(TOPIC,b"25.23")
            time.sleep(2)
    except Exception:
        mqtt.disconnect()           
            
if __name__=="__main__":
    SERVER="192.168.0.252"
    CLIENT_ID=binascii.hexlify(machine.unique_id())
    TOPIC=b"SA-58/雞舍"
    main()
    