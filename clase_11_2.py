"""Crea una clase base llamada Animal con atributos como nombre y edad.
Luego, define clases derivadas como Perro, Gato, etc., que agreguen
atributos específicos y métodos relacionados con cada tipo de animal."""


class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Perro(Animal):
    def __init__(self, nombre, edad, muerde):
        super().__init__(nombre, edad)
        self.muerde = muerde

    def morder(self):
        return f"El perro {self.nombre} muerde"

perro = Perro('asd', 12, True)
perrito = Perro('asdasd', 12, False)
print(perro.muerde)
print(perrito.muerde)

