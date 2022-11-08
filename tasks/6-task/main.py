class Veiculo:
    Color = 'red'

    Ruedas = 4

    Puertas = 2


class Coche(Veiculo):
    Velocidad = 120

    Cilindrada = 8


coche = Coche()


print('coche Color', coche.Color)
print('coche Ruedas', coche.Ruedas)
print('coche Puertas', coche.Puertas)
print('coche Velocidad', coche.Velocidad)
print('coche Cilindrada', coche.Cilindrada)
