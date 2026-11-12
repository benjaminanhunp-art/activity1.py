def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def division(a,b):
    print(a/b)

print("What do you want to do?")

operation = input("a,b,c,d ")
a = int(input("Enter the first number "))
b = int(input("Enter your second number "))

if operation == "a":
    add(a,b)

if operation == "b":
    sub(a,b)

if operation == "c":
    multiply(a,b)

if operation == "d":
    division(a,b)
