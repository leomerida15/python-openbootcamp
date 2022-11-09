class Alumno:
    notaminima = 9

    _notas = 0

    def Revicion(self):
        if self._notas > self.notaminima:
            return 'aprobado'
        else:
            return 'reprobado'

    def setNotas(self, Nota: int):
        self.notas = Nota

    def getNotas(self):
        return self.notas

    _nombre = ''

    def setNombre(self, Nombre: str):
        self.nombre = Nombre

    def getNombre(self):
        return self.nombre


alumno = Alumno()

name = str(input("Ingrese el nombre de su alumno: "))

alumno.setNombre(name)

nota = int(input(f'Ingrese la nota de {alumno.getNombre()}: '))

alumno.setNotas(nota)

print(alumno.getNombre(), ' tiene una nota de ',
      alumno.getNotas(), ' y esta ', alumno.Revicion())
