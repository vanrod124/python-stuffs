s = 'y'

while s == 'y':
    c = float(input("Enter celcius: "))
    iteration = int(input("Enter conversions: "))
    increment = int(input("Enter increment value: "))

    for i in range(iteration):
        f = (c * 9/5) + 32
        print(c, "C = ", f, "F")
        c += increment

    s = input("Do you want to continue? (y/n): ")

