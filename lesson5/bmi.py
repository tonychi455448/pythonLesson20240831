import widget

#主程式
while True:
  HEIGH,WEIGH=widget.input_data()
  BMI=widget.calculate_bmi(weight=WEIGH,heigh=HEIGH)
  print(f"您的BMI是{BMI}")
  print(widget.get_status(BMI))

  result=input("繼續?(y/n)")
  if result=="n" or result=="N":
    break
print("程式結束")
