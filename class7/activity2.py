units_consumed = int(input("How many units of electricity have you consumed: "))

if units_consumed < 50:
    amount = units_consumed*2

elif units_consumed < 100:
    amount = units_consumed*3

elif units_consumed < 200:
    amount = units_consumed*4

else:
    amount = units_consumed*5

print("bill amount: ", amount)