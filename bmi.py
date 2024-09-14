def input_data()->tuple[int,int]:
  while True:
    try:
        heigh=float(input("請輸入身高,單位為(公分):"))
        break
    except ValueError:
        print('輸入格式錯誤')
        continue
    except Exception as e:
        print(f'輸入錯誤{heigh}')
        continue
  
  while True:
     try:
        weight=float(input("請輸入體重,單位為(公斤):"))
        break
     except ValueError:
        print('輸入格式錯誤')
        continue
     except Exception as e:
        print(f'輸入錯誤{weight}')
        continue
  return (heigh,weight)

def get_status(bmi:float)->str:
  if bmi<18.5:
    return "太輕"
  elif 18.5<=bmi<25:
    return "正常"
  elif 25<=bmi<30:
    return "過重"
  else:
    return "肥胖"

#主程式
while True:
  heigh,weight=input_data()
  BMI=round(weight/(heigh/100)**2,5)
  print(f"您的BMI是{BMI}")
  print(get_status(BMI))
  
  result=input("繼續?(y/n)")
  if result=="n" or result=="N":
    break
print("程式結束")