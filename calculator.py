"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def square_root(a):
    if a < 0:
        raise ValueError("Cannot square-root negatives")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def log(a, b):
    if a <= 1:
        raise ValueError("Log base cannot be less than 2")
    if b < 1:
        raise ValueError("Cannot use log on negative numbers")
    return math.log(b, a)

#Asher   /\
#Mariana \/

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if  b ==0:
        raise ZeroDivisionError ("Cannot divide by zero")

def exp (a,b):
    return a**b

