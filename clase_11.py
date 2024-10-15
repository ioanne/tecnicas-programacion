"""Crea una clase base llamada Animal con atributos como nombre y edad.
Luego, define clases derivadas como Perro, Gato, etc., que agreguen
atributos específicos y métodos relacionados con cada tipo de animal."""


class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Perro(Animal):
    def __init__(self, nombre, edad, muerde):
        print(Perro)
        super().__init__(nombre, edad)
        self.muerde = muerde

    def mover_cola(self):
        return "mover cola"


class Gato(Animal):
    def __init__(self, nombre, edad, bufa):
        super().__init__(nombre, edad)
        self.ataca = bufa

    def escalar_arbol(self):
        return "escalando arbol"


class Leon(Animal):
    def __init__(self, nombre, edad, ataca=True):
        super().__init__(nombre, edad)
        self.ataca = ataca

    def accion_habitual(self):
        return "atacando" if self.ataca else "ronronea"
    

class Pajaro(Animal):
    pass

perrito = Perro(nombre='perrito',edad=2, muerde=True)
perrote = Perro('perrote', 5, False)

febo = Gato(nombre='febo', edad=8, bufa=True)
turing = Gato(nombre='turing', edad=7, bufa=False)

leon = Leon(nombre='leon', edad=5)
leon_manso = Leon(nombre='leon_manso', edad=5, ataca=False)

print(perrito.nombre)
print(perrito.mover_cola())

print(perrote.nombre)
print(perrote.mover_cola())


print(febo.nombre)
print(febo.escalar_arbol())

print(turing.nombre)
print(turing.escalar_arbol())

print(leon.nombre)
print(leon.accion_habitual())


print(leon_manso.nombre)
print(leon_manso.accion_habitual())


pajaro = Pajaro("pajaro", 1)
print(pajaro.nombre)