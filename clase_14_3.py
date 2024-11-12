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
        promedio = None

        try:
            promedio = sum(self._notas) / len(self._notas)
        except ZeroDivisionError:
            print("No se puede dividir por cero")
        except TypeError:
            print("No se puede sumar una lista con un string")
        else:
            print("El promedio es: ")
        finally:
            return promedio

alumno = Alumno()
alumno.agregar_nota("1")
print(alumno.notas)
print(alumno.promedio())

