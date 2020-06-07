def welcome():
    print('''
Welcome to calculator
''')
welcome()

def calculate():
    operation = input('''enter the mathematical operation you want to perform.
+ for addition
- for subtraction
* for multiplication
/ for division
''')
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))

    if operation == '+':
        print('{}+{}='.format(number1, number2))
        print(number1+numer2)

    elif operation == '-':
         print('{}-{}='.format(number1, number2))
         print(number1-numer2)

    elif operation == '*':
        print('{}*{}='.format(number1, number2))
        print(number1*number2)

    elif operation == '/':
         print('{}/{}='.format(number1, number2))
         print(number1/number2)

    else:
        print('you have chosen a wrong operator')

    again()

def again():
    calculate_again = input('''type 'y' if you want to repeat the calculation and type 'n' if you want to leave
''')
    if calculate_again == 'y':
        calculate()
    elif calculate_again == 'n':
        print('see you later...')
    else:
        again()

calculate()        
