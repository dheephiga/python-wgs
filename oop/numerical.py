class Numerical:
    def __init__(self, *args):
        self.values = args
        self.sum = sum(args)

def addition():
    num_values = int(input("Enter the number of values to add (2 or 3): "))
    if num_values == 2:
        x = int(input("Enter the value of x: "))
        y = int(input("Enter the value of y: "))
        return Numerical(x, y)
    elif num_values == 3:
        x = int(input("Enter the value of x: "))
        y = int(input("Enter the value of y: "))
        z = int(input("Enter the value of z: "))
        return Numerical(x, y, z)
    else:
       print("Number of values must be 2 or 3")
