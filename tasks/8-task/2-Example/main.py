from os import linesep


class Veiculo:
    color = ''

    transmicion = ''

    def __init__(self, color: str, transmicion: str) -> None:

        self.color = color
        self.transmicion = transmicion

    def toObj(self):
        return {"color": self.color, "transmicion": self.transmicion}


veiculo = Veiculo("azul", "automatica")


f = open('./tasks/8-task/2-Example/hola.txt', 'x')

f.close()

file = open('./tasks/8-task/2-Example/hola.txt', 'w')

for key, value in veiculo.toObj().items():
    file.write(f'{key} = {value} {linesep}')

file.close()
