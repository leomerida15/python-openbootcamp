from functools import reduce
from operator import add


N_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

N_list_impar = filter(lambda x: x % 2 != 0, N_list)

print(reduce(add, N_list_impar))
