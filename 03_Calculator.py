print('***  WELCOME TO THE PYTHON CALCULATOR  ***')

operator_1 = int(input('Enter Operator 1 : '))
operator_2 = int(input('Enter Operator 2 : '))
operand = input('       Enter Operand (+,-,*,/) : ')


if operand == '+':
    print(f'Sum of {operator_1} and {operator_2} : {operator_1+operator_2}')

elif operand == '-':
    print(f'Difference of {operator_1} and {operator_2} : {operator_1-operator_2}')

elif operand == '*':
    print(f'Multiplication of {operator_1} and {operator_2} : {operator_1*operator_2}')

elif operand == '/':
    print(f'Division of {operator_1} and {operator_2} : {operator_1/operator_2}')

else:
    print('Invalid Operation!!')


