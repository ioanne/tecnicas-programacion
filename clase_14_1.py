class Vehiculo:
    def acelerar(self):
        pass


class Auto(Vehiculo):
    def acelerar(self):
        return "Acelera de 0 a 100 en 15 segundos"


class AutoCarrera(Auto):
    def acelerar(self):
        return "Acelera de 0 a 100 en 3 segundos"


class Camion(Vehiculo):
    pass

