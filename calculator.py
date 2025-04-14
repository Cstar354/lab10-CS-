# https://github.com/Cstar354/lab10-CS-CS
# Partner 1: Camari
# Partner 2: William
# git clone https://github.com/Cstar354/lab10-CS-CS
# cd lab10-CS-
# git add calculator.py
# git commit -m "modified calculator p1"
# git push

import math

def square_root(a):
    try: 
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(a)
    except ValueError as e:
        raise e

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be > 0 and ≠ 1")
    if b <= 0:
        raise ValueError("Input must be > 0")
    return math.log(b, a)

def exp(a, b):
    return a ** b
