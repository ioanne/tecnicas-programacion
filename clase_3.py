# Las variables solo pueden empezar con _ o letras.

# Todos los datos basicos en python son inmutables.
_privado = 10
flotante = 10.2
texto = "Hola"
nulo = None
booleanos = True
booleanos2 = False

# La idea principal de una variable en mayuscula es que su valor no cambie.
DESCRIPCION = "Constantes"
"""
Hay una convención en python que nos dice que
las variables en mayuscula son valores constantes
"""


"""

"""

numero = 10 # Va a crear el 10 en memoria.
numero2 = 20 # Va a crear el 10 en memoria.

resultado = numero + numero2 # El resultado va a crear 30 en memoria
numero = 15 # Va a crear el 10 en memoria.


cadena_texto = "Hola, como andas?. " # Va a crear en memoria (125)
cadena_texto += "Yo bien" # Va a crear en memoria (150)
print(cadena_texto)


# Listas 
lista = [] # Lista vacia
lista_vacia = list()  # Lista vacia
lista_con_datos = [1,2,3,4]
lista_con_cosas = [1, "hola", 1.0, None]
lista_ = [[1,2,3], ["texto", "texto2"]]

matriz = [[1,2,3], [4,5,6], [6,7,8]] # Matriz

lista_compras = []
lista_compras.append("Papas")

lista_compras.append("Batata")

lista_compras.append("Zapallo")

# ['Papas', 'Batata', 'Zapallo']
lista_compras.pop()
# ['Papas', 'Batata']

# Diccionarios
diccionario = {}
diccionario_ = dict()

diccionario["nombre"] = "Juan"

print(diccionario["nombre"])

diccionario["lista_compras"] = lista_compras

diccionario_2 = {
    "datos_personales": {
        "nombre": "Juan"
    },
    "lista_compras": ["Banana", "Manzana", "Papas"],
    "informacion": "Pagar en efectivo"
}

diccionario_2["datos_personales"]["nombre"]
diccionario_2["lista_compras"]
diccionario_2["lista_compras"][0]
diccionario_2["lista_compras"][1]
diccionario_2["lista_compras"][2]
diccionario_2["informacion"]

# Tuplas
tupla1 = (1,2,3,4)
tupla2 = (1,)
tupla_vacia = tuple()
