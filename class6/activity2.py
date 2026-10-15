height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight/(height/100)**2

if bmi < 18.5:
    print("Underweighted")

elif bmi < 25:
    print("healthy")

else:
    print("obese")