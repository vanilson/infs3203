class Calculator:
    '''This function returns the float of adding two float operands
        :param x: x is the first float or an int number
        :param y: y is the second float or an int number
        
        #Bug(s) fixed
         -Nothing

        #Features added
         -Just the doc-string via comments
    '''
    def add(self, x : float, y: float) -> float:
        return x + y

    '''This function returns the float of subtracting two float operands
        :param x: x is the first float or an int number
        :param y: y is the second float or an int number

        #Bug(s) fixed
         -changed the operator from - to +
        
        #Features added
         -Just the doc-string via comments
    '''
    def subtract(self, x : float, y : float) -> float:
        return x - y


    '''This function returns the float of multiplying two float operands
        :param x: x is the first float or an int number
        :param y: y is the second float or an int number

        #Bug(s) fixed
         -Nothing found

        #Features added
         -Just the doc-string via comments
    '''
    def multiply(self, x : float, y : float) -> float:
        return x * y
    
    '''This function returns the float of dividing two float operands
        :param x: x is the first float or an int number
        :param y: y is the second float or an int number

        #Bug(s) fixed
         -Nothing found

        #Features added
         -Just the doc-string via comments
    '''
    def divide(self, x : float, y : float) -> float:
        if y == 0:
            return "Cannot divide by zero"
        return x / y

    '''This function returns the int of modulo between two float operands
        :param x: x is the first float or an int number
        :param y: y is the second float or an int number

        #Bug(s) fixed
         -Nothing found

        #Features added
         -Just the doc-string via comments
    '''
    def modulo(self, x : float, y : float) -> int:
        return x % y

    '''This function returns the float of the specific float power of a given float operand
        :param x: {float} x is the number float or an int number
        :param y: {float} y is the power float or an int number

        #Bug(s) fixed
         -Nothing found

        #Features added
         -Just the doc-string via comments
    '''
    def power(self, x, y) -> float:
        return x ^ y

    '''This function returns the float of square root of the given float operand
        :param x: {float} x is the float or an int number
        
        #Bug(s) fixed
         -Algorithm changed from power (1/2) to .5

        #Features added
         -Just the doc-string via comments
    '''
    def square_root(self, x) -> float:
        return x ** .5


def main():
    calc = Calculator()

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
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
