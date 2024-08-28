"""
Listas
Diccionarios
Tuplas
Conjuntos
"""



"""
A diferencia de las listas
Las tuplas son inmutables
"""
direccion_geografica = (1.12312, -3.12312)

# Podemos acceder por posicion
latitud = direccion_geografica[0]

# Podemos acceder por posicion
longitud = direccion_geografica[1]


lista_direcciones = [(1.12312, -3.12312), (2.3454, -1.5666)]



tupla = 1,2,3

tupla_vacia = tuple() # Nunca vamos a crear una tupla vacia, ya que no se puede modificar

"""
A diferencia de las listas
Los conjuntos no permite datos duplicados
Los conjutos son desordenados por ende, no tienen posicion
"""
conjunto = {1,1,1,1,2,3,4,5}


lista = [1,1,1,1,2,3,4,5]
lista_en_conjunto = set(lista)

lista_strings = ["hola", "hola", "chau"]


(True, {"blah": "asd"})
(False, {"blah": "asd"})
("10-10-90", "Nacio clemente", "peso 5 kilos")

lista = [1,2,3]

lista.sort(reverse=True)