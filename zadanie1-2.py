import math
import random
s= input('Введите "+" "-" "/" "*" "**" "модуль" "рандом" "!" "arcos"'
         '\n если возведение в степень, то запишите вторым числом степень,'
         '\n если модуль или arcos напишите 1 число, второе примите за 0')
a= int(input('первое число'))
b= int(input('второе число'))
if s in ('+', '-', '/' '*', '**', 'модуль', 'рандом', '!', 'arcos'):
    if s == '+':
        print(a+b)
    elif s == '-':
        print(a-b)
    elif s == '/':
        print(a/b)
    elif s == '*':
        print(a*b)
    elif s == '**':
        print(a**b)
    elif s == 'модуль':
        print(abs(a))
    elif s == 'рандом':
        print(random.randint(a, b))
    elif s == '!':
        print(math.factorial(a))
    elif s == 'arcos':
        print(math.acos(a))
else:
    print('прочитайте еще раз условие')