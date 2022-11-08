def validAge(age):
    # @No es Biciesto
    if age % 4 != 0 or (age % 4 == 0 and age % 100 == 0 and age % 400 != 0):
        return print("No es bisiesto")

    # @Si es Biciesto
    elif age % 4 == 0 and age % 100 != 0 or (age % 4 == 0 and age % 100 == 0 and age % 400 == 0):
        return print("Es bisiesto")


age = int(input("por favor indica el año a validar: "))

print(type(age))

validAge(age)
