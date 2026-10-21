medical_leaves = input("do you have medical leaves already? ")

if medical_leaves == "YES":
    print("approved to sit in exam")

else: 
    student_percentage = int(input("how much percentage? "))
    if student_percentage > 75:
        print("approved to sit in exam")

    else:
        print("not approved to sit in exam")