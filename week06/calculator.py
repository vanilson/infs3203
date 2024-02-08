from math import pow
#importing a the math library

class Calculator:
    def add(self, x, y):
        return x + y # Changed - to +

    def subtract(self, x, y):
        return x - y # Changed + to -

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

    def modulo(self, x, y):
        return x % y

    def power(self, x, y):
        return pow(x , y) # Bug fix

    def square_root(self, x):
        return x ** (0.5) #Bug fix

def check_ifnum(z):	# new function to validate the input by the user
    if ((z[0] in "0123456789")or((z[0] in "-0123456789" )and (z[1] in "0123456789"))):
        z=float(z)
    else:
        notFix=True
        while(notFix):
            z = input("Error, not a number. Enter a number: ")
            if ((z[0] in "0123456789")or((z[0] in "-0123456789" )and (z[1] in "0123456789"))):
                z=float(z)
                notFix=False
    return z

def main():
    calc = Calculator()

    x = input("Enter first number: ")
    x = check_ifnum(x)
    y = input("Enter second number: ")
    y = check_ifnum(y)
    operation = input("Enter operation (add, subtract, multiply, divide, modulo, power, square_root): ")

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
        print("Invalid operation")


if __name__ == "__main__":
    main()
