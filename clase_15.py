"""
Desarrolla un simulador de una ciudad donde puedas controlar aspectos
como la población, la economía, la seguridad, etc. Crea clases como
Ciudadano, Edificio, Vehículo, etc
"""
import abc


class Ciudadano:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni


class EdificioAbstracto(abc.ABC):
    @abc.abstractmethod
    def comprar_depto(self, nombre, dni):
        pass


class Edificio(EdificioAbstracto):
    def __init__(self):
        self._propietario = []

    def comprar_depto(self, nombre, dni):
        self._propietario.append(Ciudadano(nombre=nombre, dni=dni))


class EdificioResidencial(Edificio):
    pass


class EdificioComercial(Edificio):
    pass


class Vehiculo:
    def __init__(self, patente):
        self.patente = patente


class Trabajador(Ciudadano):
    def __init__(self, nombre, dni, ocupacion):
        super().__init__(nombre, dni)
        self.ocupacion = ocupacion
        self._vehiculos = []

    def vehiculos(self):
        return self._vehiculos

    def comprar_vehiculo(self, patente):
        self._vehiculos.append(Vehiculo(patente))


class Estudiante(Ciudadano):
    pass
