class Auto:
    TIPO = "Auto"

    def __init__(self, nombre):
        self.nombre = nombre
        self._es_rapido = True
        self._esta_cerrado = False

    def acelerar(self):
        # Acá puedo modificar el valor de _es_rapido
        return "Acelerando"

    @staticmethod
    def ver_codigo():
        return "Codigo de la clase Auto"

    @classmethod
    def ver_info(cls):
        return cls.ver_codigo()

    @classmethod
    def ver_tipo(cls):
        return cls.TIPO

    @property
    def es_rapido(self):
        # Chequear en base al objeto si el auto es rápido o no
        return self._es_rapido
    
    @property
    def esta_cerrado(self):
        return self._esta_cerrado
    
    def cerrar_auto(self):
        if not self.esta_cerrado:
            self._esta_cerrado = True
    
    def abrir_auto(self):
        if self.esta_cerrado:
            self._esta_cerrado = False

print(Auto.ver_codigo())

print(Auto.ver_info())
print(Auto.ver_tipo())


auto = Auto("Ferrari")
print(auto.es_rapido)
# auto.es_rapido = False # No nos permite modificar el valor de un atributo de solo lectura

# Nunca tenemos que modificar una variable privada (con _ )
# auto._es_rapido = False

class Persona:
    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    @property
    def es_mayor(self):
        # Calcular si la persona es mayor de edad
        pass


