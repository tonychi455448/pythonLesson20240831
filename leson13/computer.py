import os
import csv
from datetime import datetime

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