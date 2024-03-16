import os, time

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
         -To replace ^ (bitwise Exclusive operator) with ** (Exponenatiation Operator)

        #Features added
         -Just the doc-string via comments
    '''
    def power(self, x, y) -> float:
        return x ** y

    '''This function returns the float of square root of the given float operand
        :param x: {float} x is the float or an int number
        
        #Bug(s) fixed
         -Algorithm changed from power (1/2) to .5

        #Features added
         -Just the doc-string via comments
    '''
    def square_root(self, x) -> float:
        return x ** .5


#General variables

calculator_options : dict = {1 : 'add',
                             2 : 'subtract',
                             3 : 'multiply',
                             4 : 'divide',
                             5 : 'modulo',
                             6 : 'power',
                             7 : 'square_root',
                             0 : 'Exit the application'
                             }

instructions_msg : str = "Please select the number of the mathematical operation from the above options: "

#General functions
'''This function welcomes the user to the program
'''
def welcome() -> None:
    print('\033c')
    print(f'Welcome to {"Calculator Program":^}')

'''This function offers the choices for the user
'''
def show_options() -> str:
    for key, value in calculator_options.items():
        print(f'{key} = {value}')
    return input(instructions_msg)

'''This function gets the validated user integer entry and from the available options
    :param options_keys: Is the keys representing the options for the calculator
'''
def get_entry():
    user_entry = show_options()
    while not user_entry.isnumeric():
        user_entry = show_options()
    return int(user_entry)

'''This function gets the numbers from the user
'''
def get_numbers(times: int, first_name : str, second_name : str = None) -> list:
    entries : list = []
    msg1 = f'Enter the {first_name}: '
    msg2 = f'Enter the {second_name}: '
    entries.append(input(msg1))
    while not entries[0].isnumeric():
        entries[0] = input(msg1)
    if times == 2:
        entries.append(input(msg2))
        while not entries[1].isnumeric():
            entries[1] = input(msg2)
    entries = [int(i) for i in entries]
    return entries

'''This functions routs to the math operation matches the user's choice
    :param choice: Is the user's choice
'''
def calculate(calculator : object, choice :int):
    match(choice):
        case 1:
            user_entries = get_numbers(2, 'first number', 'second number')
            result = calculator.add(user_entries[0], user_entries[1])
            print(f'{result:,.2f}\n')
        
        case 2:
            user_entries = get_numbers(2, 'first number', 'second number to be subtracted')
            result = calculator.subtract(user_entries[0], user_entries[1])
            print(f'{result:,.2f}\n')

      
        case 3:
            user_entries = get_numbers(2, 'first number', 'second number')
            result = calculator.multiply(user_entries[0], user_entries[1])
            print(f'{result:,.2f}\n')
      
        case 4:
            user_entries = get_numbers(2, 'dividend', 'divisor')
            result = calculator.divide(user_entries[0], user_entries[1])
            print(f'{result:,.2f}\n')

        case 5:
            user_entries = get_numbers(2, 'dividend', 'devisor')
            result = calculator.modulo(user_entries[0], user_entries[1])
            print(f'{result:,.2f}\n')

        case 6:
            user_entries = get_numbers(2, 'base', 'exponent')
            result = calculator.power(user_entries[0], user_entries[1])
            print(f'{result:,.2f}\n')

        case 7:
            user_entries = get_numbers(1, 'base number')
            result = calculator.square_root(user_entries[0])
            print(f'{result:,.2f}\n')


'''This is the main function of the program
'''
def main():
    welcome()
    calc = Calculator()
    choice : int = get_entry()
    while choice != 0:
        calculate(calc, choice)
        choice = get_entry()
    os.system('clear')
    print('Thank you for using our Calculator\nWe hope to see you again\U0001F31E')
    time.sleep(3)
    os.system('clear')

if __name__ == "__main__":
    main()
