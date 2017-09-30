from functools import *


def f1(x):
    return x % 2 == 0


def f2(x):
    return x > 4


def m1(x):
    return x + 1


def m2(x):
    return x - 6


def m3(x):
    return abs(x)  # abs jest to moduł


def r1(x, y):
    return x * y


def r2(x, y):
    return x + y


l = list(range(20))
l = list(map(m1, l))
l = list(filter(f1, l))
l = list(map(m2, l))
l = list(filter(f2, l))
l = reduce(r2, l)
print(l)

l = list(range(20))
l = list(map(lambda x: x + 1, l))  # lambda jest to mała funkcja której nie ma potrzeby definiowania
l = list(filter(lambda x: x % 2 == 0, l))
l = list(map(lambda x: x - 6, l))
l = list(filter(lambda x: x > 4, l))
l = reduce(r2, l)
print(l)

l = [x + 2 for x in range(6) if x % 2 == 0]
print(l)
print('ala'.replace('a',''))