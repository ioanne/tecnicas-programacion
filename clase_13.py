"""2.10
Imagina que estás desarrollando un sistema de gestión para una compañía
de transporte. Tu objetivo es diseñar un conjunto de clases orientadas a
objetos para manejar vehículos, rutas, conductores y clientes. Debes crear
clases como 'Vehiculo', 'Ruta', 'Conductor' y 'Cliente'. Implementa herencia
para representar diferentes tipos de vehículos, como 'Automovil' y 'Camion'.
Utiliza la composición para gestionar la relación entre rutas, conductores y
clientes, y asegúrate de que el diseño sea escalable para futuras
funcionalidades del sistema de transporte."""

from abc import ABC, abstractmethod


class VehiculoAbstracto(ABC):
    def __init__(self):
        pass
    

    @abstractmethod
    def obtener_capacidad(self) -> int | float:
        pass


class Vehiculo(VehiculoAbstracto):
    def __init__(self, dni):
        self.dni_conductor = dni


class Auto(Vehiculo):

    def obtener_capacidad(self):
        return 1000


class Camion(Vehiculo):
    def __init__(self):
        pass

    def obtener_capacidad(self):
        return 10000


class Moto(Vehiculo):
    def obtener_capacidad(self):
        return 100
    

vehiculos_empresa = [
    Auto(dni_conductor=12345678),
    Camion(dni_conductor=12345678),
    Auto(dni_conductor=12345678),
    Camion(dni_conductor=12345678),
    Camion(dni_conductor=12345678),
    Camion(dni_conductor=12345678),
    Moto(dni_conductor=12345678),
    Moto(dni_conductor=12345678),
    Moto(dni_conductor=12345678),
    Moto(dni_conductor=12345678),
]

peso_maximo = 0
for vehiculo in vehiculos_empresa:
    peso_maximo += vehiculo.obtener_capacidad()

print(f'El peso máximo es: {peso_maximo}')


class Ruta:
    def __init__(self, direccion, paquete):
        self.direccion = direccion
        self.paquete = Paquete(**paquete)


class Conductor:
    def __init__(self, dni, tipo_vehiculo):
        self.rutas = []
        if tipo_vehiculo == 'auto':
            self.vehiculo = Auto(dni_conductor=dni)
        elif tipo_vehiculo == 'camion':
            self.vehiculo = Camion(dni_conductor=dni)
        elif tipo_vehiculo == 'moto':
            self.vehiculo = Moto(dni_conductor=dni)
    
    def obtener_rutas(self, planilla_rutas):
        self.rutas = []
        for ruta in planilla_rutas:
            self.rutas.append(Ruta(**ruta))


class Paquete:
    def __init__(self, peso, cliente):
        self.peso = peso
        self.cliente = Cliente(**cliente)


class Cliente:
    def __init__(self):
        pass
