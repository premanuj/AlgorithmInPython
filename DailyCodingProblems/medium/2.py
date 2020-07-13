"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(func):
    def inner(*num):
        return num[0]
    return func(inner)

def cdr(func):
    def inner(*num):
        return num[-1]
    return func(inner)

if __name__ == "__main__":
    a, b = [int(i.strip()) for i in input("Enter the number for a and b: ").split(",")]
    print("CAR: ", car(cons(a,b)))
    print("CDR: ", cdr(cons(a,b)))