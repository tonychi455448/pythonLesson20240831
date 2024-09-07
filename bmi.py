heigh=int(input("請輸入身高,單位為(公分):"))
weight=int(input("請輸入體重,單位為(公斤):"))

bmi=round(weight/(heigh/100)**2,5)
print(f"您的BMI是{bmi}")

if bmi<18.5:
    print("太輕")
elif 18.5<=bmi<25:
    print("正常")
elif 25<=bmi<30:
    print("過重")
else:
    print("肥胖")