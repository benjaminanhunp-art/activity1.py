actual_cost = float(input("enter the actual cost of the shoes: "))
selling_cost = float(input("enter the selling cost of the shoes: "))

if selling_cost > actual_cost:
    print("profit")

if selling_cost < actual_cost:
    print("loss")