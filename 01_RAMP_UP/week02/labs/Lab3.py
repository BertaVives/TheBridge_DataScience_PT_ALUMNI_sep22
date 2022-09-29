while True: 
    try:
        a = int(input('First number?'))
        break
    except ValueError:
        print('Please input a number')
op = str(input('Operation?'))
while True: 
    try:
        b = int(input('First number?'))
        break
    except ValueError:
        print('Please input a number')

operadores = ['+','-','*','/','//','%']

if op in operadores:
    if op == '+':
        result = a+b
    elif op == '-':
        result = a-b
    elif op == '*':
        result = a*b
    elif op == '/':
        result = a/b
    elif op == '//':
        result = a//b
    elif op == '%':
        result = a%b
    print(a, ' ', op, ' ', b, ' equals ', result)
else:
    print('Operación no reconocida')