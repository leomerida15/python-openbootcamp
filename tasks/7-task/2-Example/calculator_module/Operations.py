from operator import add, sub, mul, truediv
from functools import reduce


def Suma(*Ns):
    return reduce(add, Ns)


def Resta(*Ns):
    return reduce(sub, Ns)


def Multiplica(*Ns):
    return reduce(mul, Ns)


def Divide(*Ns):
    return reduce(truediv, Ns)
