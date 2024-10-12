import os
import csv
from datetime import datetime
import paho.mqtt.client as mqtt

# Define the callback function for when a message is received
# 定義回呼函式,負責bloker收到topic訊息

def on_message(mosq, obj, msg):
    print("topic:{0},payload:{1},qos:{2}".format(msg.topic,msg.payload.decode('utf-8'),msg.qos)) #msg.payload是binary string
    
# Define the callback function for when the client connects to the broker
# 定義回呼函式,負責處理當clent連線至broker時
def on_connect(client, userdata, flags, rc,properties=None):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic once connected
    client.subscribe("SA-58/#")
    
def main():
    os.path.abspath(__name__)
    #os.path.realpath(__file__)
    root_dir=os.getcwd()
    data_path=os.path.join(root_dir,"data")

    if not (os.path.isdir(data_path)):
        print("資料夾不存在")
        os.mkdir("data")

    # 獲取當前時間並格式化為字串
    current_date = datetime.today().strftime("%Y-%m-%d")
    filename = f"{current_date}.csv"
    filepath=os.path.join(data_path,filename)

    current_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    # 定義 CSV 標題
    header = ['時間', '設備', '值']

    if not (os.path.exists(filepath)):
        # 創建 CSV 檔案並寫入標題
        with open(filepath, mode='w', encoding='utf-8-sig', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(header)  # 寫入標題行

            # 可選：寫入一些示範數據
            csvwriter.writerow([current_time, '設備A', 100])
            csvwriter.writerow([current_time, '設備B', 200])
            print(f"CSV 檔案 '{filename}' 已建立。")
    else:
        with open(filepath, mode='a', encoding='utf-8-sig', newline='') as csvfile:
            # 可選：寫入一些示範數據
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([current_time, '設備c', 300])
            csvwriter.writerow([current_time, '設備d', 400])
            print(f"CSV 檔案 '{filename}' 已存在。")
    pass

if __name__ == "__main__":
	#必需使用VERSION2,VERSION1已經Deprecation
	client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
	client.on_message = on_message
	client.on_connect = on_connect
	
	# Set user ID and password
	client.username_pw_set("pi", "raspberry")
	
	#SSL連線
	#client.tls_set('root.ca', certfile='c1.crt', keyfile='c1.key')
    # 	
	# Connect to the broker (replace 'broker_address' with the address of your MQTT broker)
	client.connect("192.168.0.252", 1883, 60)

	client.loop_forever()
    