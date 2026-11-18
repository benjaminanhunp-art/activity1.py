def circumference(radius):
    pi = 3.14
    result = 2 * pi * radius
    print("The circumference of the circle is:", round(result, 2))


radius = float(input("Enter the radius of the circle: "))

# Call the function
circumference(radius)
