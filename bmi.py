import tools

#主程式
while True:
  HEIGH,WEIGH=tools.input_data()
  BMI=tools.calculate_bmi(weight=WEIGH,heigh=HEIGH)
  print(f"您的BMI是{BMI}")
  print(tools.get_status(BMI))

  result=input("繼續?(y/n)")
  if result=="n" or result=="N":
    break
print("程式結束")