#!/usr/bin/env python3.14
#calc
import os
import math

c = str('y')
r = float(0.0)
r2 = float(0.0)
print('Calc 1.0\ntype "help" for instructions, or "exit" to close the program')
while c == 'y':
    usinp = str(input())

    if '+' in usinp:
        parts = usinp.split('+')
        x = float(parts[0])
        y = float(parts[1])
        r = float(x + y)
        print(r)
    elif '-' in usinp:
        parts = usinp.split('-')
        x = float(parts[0])
        y = float(parts[1])
        r = float(x - y)
        print(r)
    elif '*' in usinp:
        parts = usinp.split('*')
        x = float(parts[0])
        y = float(parts[1])
        r = float(x * y)
        print(r)
    elif '/' in usinp:
        parts = usinp.split('/')
        x = float(parts[0])
        y = float(parts[1])
        r = float(x / y)
        r2 = float(x % y)
        print('The result is: {}\nThe rest is {}'.format(r, r2))
    elif '^' in usinp:
        parts = usinp.split('^')
        x = float(parts[0])
        y = float(parts[1])
        r = float(math.pow(x, y))
        print(r)
    elif 'help' in usinp:
        print('"+"  to sum\n"-" to subtract\n"*" to multiply\n"/" to divide\n"^" to exponentiate\n"clear" to clear the screen\n"exit" to close')
    elif 'exit' in usinp:
        c = str ('n')
    elif 'clear' in usinp:
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('Invalid command | "help" for instructions or "exit" to close')

