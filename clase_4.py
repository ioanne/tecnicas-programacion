"""
1. Crear una lista con 10 valores
Crea una lista llamada valores que contenga 10 valores numéricos de tu
elección.
Documenta el código explicando qué estás haciendo en cada paso.
"""

# Estamos declarando una variable llama valores que contiene 10 valores numericos.
valores = [1,2,3,4,5,6,7,8,9,0] 
print(valores)
"""
2. Agregar valores a una lista
Crea una lista con 5 valores.
Luego, agrega 3 valores adicionales a la lista usando el método append()
Documenta el proceso de adición de los nuevos valores.
"""

# Declaramos una variable llamada lista1 y le almacenamos una lista de enteros.
lista1 = [1,2,3,4,5]

# Agregamos el string Hola a lista1.
lista1.append("Hola")

# Agregamos el valor 6 a lista1.
lista1.append(6)

# Agregamos el valor 8 a lista1.
lista1.append(8)
print(lista1)



"""
3. Combinar dos listas
Crea dos listas: una llamada nueva_lista con 5 valores y otra llamada lista2
con 2 valores.
Combina ambas listas usando el método extend en nueva_lista para que esta
lista contenga todos los elementos.
Documenta cómo has combinado las listas y explica el resultado.
"""


nueva_lista = [1,2,3,4,5]
lista2 = [3,5, "hola", None, True]

# Agregamos los valores de lista2 dentro de nueva_lista
nueva_lista.extend(lista2)

# otra manera de concatenar listas es usando +
# Unicamente se puede hacer si ambos valores son listas.
nueva_lista += lista2

print(nueva_lista)
print(lista2)

"""
4. Eliminar el último valor de una lista
Crea una lista llamada numeros que contenga 8 valores.
Luego, elimina el último valor de la lista utilizando el método pop().
Documentar cómo funciona.
"""

# Tambien se puede multiplicar una lista
print(["Hola"] * 2)

# Se pueden multiplicar las cadenas de caracters.
print("Hola" * 2)

"""
5. Acceder a un valor en una posición específica
Utilizando la lista que creaste en el ejercicio 1, muestra el valor que se
encuentra en la tercera posición (recuerda que las listas en Python
empiezan en la posición 0).
Documenta el proceso de acceso a un valor específico de una lista.
"""

print(valores[2])

"""
6. Mostrar el último valor de una lista
Usando la lista que creaste en el ejercicio 1, muestra el último valor de la
lista.
Documenta las diferentes formas en que puedes acceder al último valor
de una lista.
"""

print(valores[-len(valores) - 1])
# print(valores[9])
# print(valores[-1])
# print(valores)
# print(valores.pop())
# print(valores)


# print(valores[0])