# https://github.com/Cstar354/lab10-CS-
# Partner 1: Camari
# Partner 2: William
# git clone https://github.com/Cstar354/lab10-CS-
# cd https://github.com/Cstar354/lab10-CS-
# git add calculator.py
# git committ - m "modified calculator p1"
# git push


import math
def square_root(a):
    try: 
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError as e:
        raise e
def hyptenuse(a,b):
    math.hypot(a,b)

def add(a,b): 
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
     if a==0 
        raise ZeroDivisionError
    return a/b
def logarithm(a,b):
    if a<=0 or a==1
        raise ValueError
    if b <= 0
        raise ValueError
    return math.log(b,a)

def exponent(a,b):
    return a**b
    
