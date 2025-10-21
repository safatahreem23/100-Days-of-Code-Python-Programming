#BMI Calculator- users body mass based on their height and weight
height = 1.65
weight = 84

bmi = weight/(height**2)
print(bmi)
print(int(bmi))

#same program by taking height and width from keyboard
height = float((input("enter your height?")))
weight = float((input("enter your weight?")))

bmi = weight/(height**2)
print(bmi)

#this is called as floor a number/remove all decimal points using int
print(int(bmi))

#round()function- rounding the nearest values
print(round(bmi))
print(round(bmi,2))# rounding 2 digits instead of nearest number