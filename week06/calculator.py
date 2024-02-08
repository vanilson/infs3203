class Calculator:
    def add(self, x, y):
        return x - y

    def subtract(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

    def modulo(self, x, y):
        return x % y

    def power(self, x, y):
        return x ^ y

    def square_root(self, x):
        return x ** (1 / 2)

"""
This function is used to get the numbers from the user that they want to perform the operation on.
If the type of operation requires two numbers, it will prompt the user to enter two numbers. Else, it will prompt the user to enter one number.
"""
def get_entries(operation, num_of_entries = 2):
    if num_of_entries == 2:
        x = float(input(f"Enter first number for the {operation} operation: "))
        y = float(input("Enter second number: "))
        return x, y
    else:
        x = float(input("Enter a number: "))
        return x

"""
This is the main file that will use the Calculator class to perform operations on numbers.
It contains a prompt for the user to enter the operation they want to perform and the numbers they want to perform the operation on.
Based on the entered operation, the program will call the appropriate method of the Calculator class to perform the operation.
"""
def main():
    calc = Calculator()
    operation = input("Enter operation (add, subtract, multiply, divide, modulo, power, square_root): ")

    if operation == "add":
        print(calc.add(*get_entries("add")))
    elif operation == "subtract":
        print(calc.subtract(*get_entries("subtract")))
    elif operation == "multiply":
        print(calc.multiply(*get_entries("multiply")))
    elif operation == "divide":
        print(calc.divide(*get_entries("divide")))
    elif operation == "modulo":
        print(calc.modulo(*get_entries("modulo")))
    elif operation == "power":
        print(calc.power(*get_entries("power")))
    elif operation == "square_root":
        print(calc.square_root(get_entries("square_root", 1)))
    else:
        print("Invalid operation")


if __name__ == "__main__":
    main()
