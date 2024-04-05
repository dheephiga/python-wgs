'''Create a module called math_operations.py
containing functions for addition, subtraction, multiplication, and
division. Then write a program that imports this module and uses
these functions.'''

def addition(a,b):
    if(a.isdigit() and b.isdigit()):
        print(a+b)
    
    else:
        print("Invalid input")

def subtraction(a,b):
    if(a.isdigit() and b.isdigit()):
        print(a-b)
    
    else:
        print("Invalid input")

def multiplication(a,b):
    if(a.isdigit() and b.isdigit()):
        print(a*b)
    
    else:
        print("Invalid input")

def division(a,b):
    if(a.isdigit() and b.isdigit()):
        if(a!=0 and b!=0):
            print(a/b)
    
    else:
        print("Invalid input")


