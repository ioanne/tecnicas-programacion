# Por convención las clases comienzan con Mayuscula no llevan _
# Y Si tenemos un nombre compuesto VaEnMayuscula

# Clase basica llamada Auto
class Auto:
    # Receta para crear objetos
    pass

# Creamos un objeto a partir de la clase Auto
auto = Auto() # Instanciar -> Crear un objeto
auto2 = Auto()
auto3 = Auto()

print(auto)
print(auto2)
print(auto3)


class AlumnoAbstracto:
    # Primero parametro es la referencia a si mismo y se llama self
    def __init__(self, nombre, apellido, nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
    
    def resolver_parcial(self):
        pass

    def consultar_nota(self):
        pass


class Alumno(AlumnoAbstracto):
    def resolver_parcial(self):
        return "Resolviendo parcial"

    def consultar_nota(self):
        return "Consultando nota"

alumno = Alumno(nombre="Juan", apellido="Perez", nacimiento="01/01/1990")
alumno_2 = Alumno(nombre="Maria", apellido="Gomez", nacimiento="01/05/1986")
print(alumno.resolver_parcial())
print(alumno_2.consultar_nota())


print()
