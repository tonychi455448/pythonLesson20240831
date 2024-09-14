while True:
  while True:
    try:
        heigh=float(input("請輸入身高,單位為(公分):"))
        break
    except:
        print("輸入錯誤")
        continue
  
  while True:
     try:
        weight=float(input("請輸入體重,單位為(公斤):"))
        break
     except:
        print("輸入錯誤")
        continue
    
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

  result=input("繼續?(y/n)")
  if result=="n":
    break
print("程式結束")