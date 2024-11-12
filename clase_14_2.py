class Persona:
    pass


class Alumno(Persona):
    def __init__(self):
        self._notas = None
    
    @property
    def notas(self):
        return self._notas
    
    def agregar_nota(self, nota):
        if self._notas is None:
            self._notas = []
        if isinstance(nota, int) and nota >= 0 and nota <= 10:
            self._notas.append(nota)

    def promedio(self):
        if self._notas is None and sum(self._notas) == 0:
            return None
        return sum(self._notas) / len(self._notas)

alumno = Alumno()
print(alumno.notas)
alumno.agregar_nota(8)
alumno.agregar_nota(6)
alumno.agregar_nota(9)
print(alumno.notas)
print(alumno.promedio())
alumno._notas = "batata"
print(alumno.notas)
print(alumno.promedio())
