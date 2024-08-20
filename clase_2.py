# Trabajando con strings 1
nombre = "Juan"
apellido = "Bonini"


nombre_completo = nombre + " " + apellido # Concatenación de strings

print(nombre_completo)


# Trabajando con strings 2

nombre = "Juan"
apellido = "Bonini"

nombre_completo = "{} {}".format(nombre, apellido)

print(nombre_completo)


# Trabajando con string 3

nombre = "Juan"
apellido = "Bonini"

nombre_completo = f"{nombre} {apellido}" # f-string

print(nombre_completo)


nombre_completo = nombre + " " + apellido # Menos usado

nombre_completo = "{} {}".format(nombre, apellido)
nombre_completo = f"{nombre} {apellido}"


formato_nombre = "{} {}"

nombre_completo_1 = formato_nombre.format("Juan", "Perez")
nombre_completo_2 = formato_nombre.format("Juan", "Gomez")
nombre_completo_3 = formato_nombre.format("Juan", "Fernandez")
nombre_completo_4 = formato_nombre.format("Juan", "Apellido")

print(nombre_completo_1)
print(nombre_completo_2)
print(nombre_completo_3)
print(nombre_completo_4)


# Si tenemos una funcion 

algo = "una suma"
formato_devuelto = "dato: informacion"
caracteres_maximos = 30

prompt = f"Necesito saber el resultado de {algo}. \n"
prompt += f"Necesito que me lo devuelvas en el formato {formato_devuelto} \n"

prompt += f"Necesito que me lo devuelvas en el formato {formato_devuelto} \n"
prompt += f"Como maximo la respuesta tiene que tener {caracteres_maximos} caracteres\n"

print(prompt)


"""
Declarar variables
Agregarle información a las variables sin perder el dato anterior +=
Declarar 2 variables con datos, y almacenar en otra variable el resultado
    Esto lo hacemos para cada tipo de operacion + - * / 

Documentar con comentarios el codigo
"""


# Operadores de comparación
# >
# <
# >=
# <=
# ==
# !=

# Operadores lógicos
# AND   Y
# OR    O
# NOT   Negacion

# bool  --> boolean
# De que viene la palabra bool?
# Algebra de boole

n1 = 20
n2 = 102

if n1 >= n2: # Si n1 es mayor o igual a n2
    print('N1 es mayor que n2')
    print(1)
    print(2)
    print(3)
print(4)





valor_1 = 10
valor_2 = 50



# if (condicion):
#    ...
#    ...
#    ...


# Siempre que querramos evaluar para probar si devuelve verdadero o falso
# Tenemos que usar la función de python bool.
if valor_1 > valor_2: # Si valor 1 es 10 y valor 2 es 50, no se cumple la condición
    print(valor_1) 


if valor_2 > valor_1:
    print(valor_2)



if valor_1 == valor_2:
    print(valor_1, valor_2)
    

bananas = 20
manzanas = 20

# Queremos hacer un licuado de bananas y manzanas
if bananas and manzanas:
    print('Podemos hacer un licuado de bananas y manzanas')

if bananas or manzanas:
    if bananas:
        print('Podemos hacer licuado de banana')

    if manzanas:
        print('Podemos hacer licuado de manzanas')


# Evaluaciones
# número positivo mayor a 0 evalua True / Verdadero
# número negativo menor a 0 evalua True / Verdadero
# 0 evalua False / Falso

# La palabra "Hola" evalua True / Verdadero
# Tengo un string vacio "" evalua False / Falso


numero = 15

if numero > 0:
    print('Numero es mayor que 0')

if numero != 0:
    print('Numero es mayor que 0')

if numero: # -n / n+ 
    print('Hay numero positivo o negativo. Pero es distinto a 0')

