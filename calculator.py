import math


class Calculator:
    def add(self, x, y):
        return x + y  # Corrected operation

    def subtract(self, x, y):
        return x - y  # Corrected operation

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")  # Raising an exception
        return x / y

    def modulo(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")  # Handling division by zero
        return x % y

    def power(self, x, y):
        return x ** y  # Corrected operator for power operation

    def square_root(self, x):
        if x < 0:
            raise ValueError("Cannot take the square root of a negative number")  # Handling negative numbers
        return x ** (1 / 2)


def main():
    calc = Calculator()
    while True:  # Loop to handle invalid inputs
        try:
            x = float(input("Enter first number: "))
            y = None
            operation = input("Enter operation (add, subtract, multiply, divide, modulo, power, square_root): ")

            # For operations that require two operands, prompt for the second operand
            if operation != "square_root":
                y = float(input("Enter second number: "))

            if operation == "add":
                print(calc.add(x, y))
            elif operation == "subtract":
                print(calc.subtract(x, y))
            elif operation == "multiply":
                print(calc.multiply(x, y))
            elif operation == "divide":
                print(calc.divide(x, y))
            elif operation == "modulo":
                print(calc.modulo(x, y))
            elif operation == "power":
                print(calc.power(x, y))
            elif operation == "square_root":
                print(calc.square_root(x))
            else:
                print("Invalid operation. Please try again.")
                continue  # Re-prompt the user for operation

            # Exit the loop after a successful operation
            break

        except ValueError as e:
            print(e)
            print("Please try again.")
        except Exception as e:
            print("An unexpected error occurred:", e)
            print("Please try again.")


if __name__ == "__main__":
    main()
