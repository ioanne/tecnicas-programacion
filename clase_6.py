"""
Encontrar el valor máximo en una lista
Utiliza una lista de números enteros. Escribe un condicional que compare
todos los valores de la lista y determine cuál es el valor máximo.
Documenta el proceso de comparación y el valor máximo encontrado.
"""

# lista_numeros = [5,4,5,6,100,4,55,3424,234,4,5454,3,4,55,543]

# valor_maximo = 0

# for numero in lista_numeros:
#     if numero > valor_maximo:
#         print(numero)
#         valor_maximo = numero
# print(f"El valor {valor_maximo} es el más grande")



























"""
Bucles (Repeticion)
"""

# for
# while

contador = 0
while contador < 5:
    print('Ejecución')
    contador +=1

# Imprime 5 veces la palabra Ejecución

contador = 0
while contador < 5:
    if contador == 2: # Condición
        contador +=1
        continue # Saltear
    print('Ejecución')
    contador +=1

# Imprime 4 veces la palabra Ejecución


contador = 0
while contador < 5:
    if contador == 2:
        break # deja de ejecutar
    print('Ejecución')
    contador +=1
# Imprime 2 veces la palabra Ejecución

"""
Pruebas de escritorio

Contador | continua
    0         True
    1         True
    2         False
"""
lista_valores = [1,2,3,4,5,6,7,8,9]

for numero in lista_valores:
    print(numero)

for numero in lista_valores:
    if numero == 3:
        continue
    print(numero)

for numero in lista_valores:
    if numero == 3:
        break
    print(numero)


# Palabra reservada break
# Sirve para romper el bucle


# Palabra reservada continue
# Sirve para saltear una ejecución


# For para cada elemento de una lista
# While mientras se cumpla la condición



""". Clasificación de números en pares e impares
Dada una lista de números enteros, escribe un condicional que clasifique
los números en dos listas separadas: una para los pares y otra para los
impares.
Documenta cómo se realiza la clasificación y muestra ambas listas
resultantes.
"""


lista_de_numeros = [2,4,5,67,45,34,0,23,2,5,6,12,3,7,6,5,4,3]

numeros_impares = []
numeros_pares = []
for n in lista_de_numeros:
    if n % 2 == 0:
        numeros_pares.append(n)
    else:
        numeros_impares.append(n)
print(f"Los numeros pares son: {numeros_pares}")
print(f"Los numeros impares son: {numeros_impares}")


"""
Verificar la existencia de un valor en varias listas
Crea tres listas llamadas lista1, lista2, y lista3, cada una con 5 valores
numéricos.
Escribe un condicional que verifique si un número específico se encuentra
en al menos una de las listas.
Documenta el proceso de verificación y cuál lista contiene el valor.
"""

lista1 = [2,3,4,5,6]
lista2 = [6,7,8,9,5]
lista3 = [10,2,3,5,6]

valor = 5
# Existe en al menos 1 lista.
existe = valor in lista1 or valor in lista2 or valor in lista3
print(existe)

# Manera 2
valores = lista1 + lista2 + lista3
existe2 = valor in valores
print(existe2)


existe_en_todas = valor in lista1 and valor in lista2 and valor in lista3
print(existe_en_todas)


def mi_funcion(valor1):
    existe1 = valor1 in lista1 and valor1 in lista2 and valor1 in lista3
    return existe1

print(mi_funcion(7))
print(mi_funcion(5))
print(mi_funcion(6))
print(mi_funcion(12))


"""
Sintaxis de una funcion es:
La palabra reservada def (definir)
luego el nombre de la funcion
y entre parentesis puede o no recibir argumentos
"""

def foo():
    return 1+5

print(foo())
