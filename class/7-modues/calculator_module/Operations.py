from functools import reduce
from operator import add, sub


def Suma(*Ns):
    return reduce(add, Ns)


def Resta(*Ns):
    return reduce(sub, Ns)
