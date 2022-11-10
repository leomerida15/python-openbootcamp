from os import linesep

file = open('hola.txt', 'w')

file.write("Primera línea" + linesep)
file.write("Segunda línea")

file.close()
