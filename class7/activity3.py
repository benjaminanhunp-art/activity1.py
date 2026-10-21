vehicle = input("which type of vehicle do you want to rent? 1. Bike  2. Car ")

if vehicle == "bike":
    bike_type = input("1. Scooter 2. Motorbike: ")
    if bike_type.lower() == "scooter":
        print("you have rented a scooter")

    else:
        print("you have rented a motorbike")

if vehicle.lower() == "car":
    car_type = input("1. sedan  2. SUV: ")
    if car_type == "sedan":
        print("you have rented a sedan")

    else:
        print("you have rented an SUV")