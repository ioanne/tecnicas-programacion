"""Implementa una clase Garage que tenga una lista de Vehículos"""


class Vehiculo:
    def __init__(self, patente):
        self.patente = patente


class Garage:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, patente):
        # La instancia se cree acá.
        self.vehiculos.append(Vehiculo(patente))

    
garage = Garage()
garage.agregar_vehiculo("ABC123")
garage.agregar_vehiculo("FGH123")
garage.agregar_vehiculo("ZZT567")

print(garage)

"""
Composición: una clase tiene una lista de objetos de otra clase

Garage "tiene" vehiculos
Garage "tiene un" vehiculo
"""


class Auto(Vehiculo):
    def __init__(self, patente):
        super().__init__(patente)

# El auto "ES UN" vehiculo


class Camioneta(Vehiculo):
    def __init__(self, patente, marca):
        super().__init__(patente)
        self.marca = marca


class Marca:
    def __init__(self, nombre):
        self.nombre = nombre


class AutoBMW(Auto): # La clase se crea una unica vez
    marca = Marca("BMW") # Acá se crea el objeto Marca con el valor BMW
    variable = [1,2,3]

auto1 = AutoBMW("ABC123")
auto2 = AutoBMW("FGH123")

print(id(auto1))
print(id(auto1.marca))

print(id(auto2))
print(id(auto2.marca))


class A:
    pass

variable = A()
variable2 = A()