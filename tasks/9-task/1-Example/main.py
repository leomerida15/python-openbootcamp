countrys = str(
    input('inserte una lista de paises separados por comas: ')).replace(' ', '').split(',')

countrys.sort()

countrys

print(', '.join(countrys))
