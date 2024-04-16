"""This program gives the user a menu-driven interface for a calculator
Also capable of doing custom operations as required by the user."""

import re

class Calculator:
# The function get_input() formats the user input from string to float datatype,
# since float is safer, if int is used, we may encounter type conversion errors
# and the function also ensures that no input other than numbers is used for operations

    def get_input(self, userInput):
        numbers = []
        for i in userInput:
            try:
                value = float(i)
                numbers.append(value)
            except ValueError:
                print(f"{i} is not of numeric type, skipping input")
                continue
        return numbers

# The function add(), returns the sum of list of numbers
    def add(self, num):
        return sum(num)

# The function subtract(), returns the difference of list of numbers

    def subtract(self, num):
        numberDifference = num[0]
        for i in num[1:]:
            numberDifference -= i
        return numberDifference

# The function mutiply(), returns the product of list of numbers

    def multiply(self, num):
        product = num[0]
        for i in num[1:]:
            product *= i
        return product

# The function division(), returns the quotient of list of numbers

    def division(self, num):
        if 0 in num:
            print("Identified 0 in input, eliminating occurrences of 0")
        if len(num) == num.count(0):
            return "Error: Division by zero!"
        quotient = num[0]
        for i in num[1:]:
            if i != 0:
                quotient /= i
        return quotient
    
    def evaluate_operation(self, operator, x, y):
        custom = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            "**": lambda x, y: x ** y,
            "//": lambda x, y: x // y,
            "%": lambda x, y: x % y,
        }
        return custom[operator](x, y)

    def custom_operations(self, expr):
        items = re.findall(r'[\d.]+|[\+\-\*/\(\)\*\*//%]', expr)  # Split the expression into tokens
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3, '//': 3, '%': 3}
        output_queue = []
        operator_stack = []

        for item in items:
            if item in precedence:
                while operator_stack and precedence.get(operator_stack[-1], 0) >= precedence[item]:
                    output_queue.append(operator_stack.pop())
                operator_stack.append(item)
            else:
                output_queue.append(item)

        while operator_stack:
            output_queue.append(operator_stack.pop())

        stack = []
        for token in output_queue:
            if token in precedence:
                if len(stack) < 2:
                    raise ValueError("Incomplete Expression")
                y = stack.pop()
                x = stack.pop()
                result = self.evaluate_operation(token, x, y)
                stack.append(result)
            else:
                stack.append(float(token))  # Convert token to float before pushing into stack

        if len(stack) != 1:
            raise ValueError("Invalid Expression")

        return stack[0]



calc = Calculator()
while True:
    print(
        "Please enter your choice\n"
        + "1 -> Addition\n"
        + "2 -> Subtraction\n"
        + "3 -> Multiplication\n"
        + "4 -> Division\n"
        + "5 -> Custom Operation\n"
        + "0 -> Exit"
    )

    userChoice = int(input("Choice: "))

    if userChoice == 0:
        break

    if 1 <= userChoice <= 4:
        print("Please enter your values: ")
        userInput = input().split()
        num = calc.get_input(userInput)

        if userChoice == 1:
            print(f"Sum is {calc.add(num)}")

        elif userChoice == 2:
            print(f"Difference is {calc.subtract(num)}")

        elif userChoice == 3:
            print(f"Product is {calc.multiply(num)}")

        elif userChoice == 4:
            print(f"Answer is {calc.division(num)}")

    elif userChoice == 5:
        expr = input("Enter custom expression (e.g., '0 * 8 / 5'): ")
        result = calc.custom_operations(expr)
        print(f"Result of custom expression {expr} is {result}")


    else:
        print("Please choose a valid choice from the menu")
