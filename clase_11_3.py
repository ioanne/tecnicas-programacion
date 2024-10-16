"""Define una clase Figura con métodos como calcular_area() y
calcular_perimetro(). Luego, crea clases derivadas como Triangulo,
Cuadrado, etc., que sobrescriban estos métodos para calcular el área y
perímetro de cada figura."""


class Figura:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass


class Triangulo(Figura):
    def __init__(self, base, altura, lado):
        self.base = base
        self.altura = altura
        self.lado = lado

    def calcular_area(self):
        return self.base * self.altura / 2
    
    def calcular_perimetro(self):
        return self.lado * 3

triangulo = Triangulo(10, 20, 10)
print(triangulo.calcular_area())
print(triangulo.calcular_perimetro())


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2
    
    def calcular_perimetro(self):
        return self.lado * 4

cuadrado = Cuadrado(10)
print(cuadrado.calcular_area())
print(cuadrado.calcular_perimetro())