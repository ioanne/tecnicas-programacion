# # Funcion
# def sumar(n1, n2):
#     return n1 + n2

# # Codigo
# numero1 = 10
# numero2 = 40

# # uso de funcion
# print(sumar(numero1, numero2))

# # Codigo
# numero5 = 123
# numero6 = 989


# # uso de funcion
# print(sumar(numero5, numero6))


# def sumar_valores(valores):
#     """Suma una lista de valores"""
#     suma = 0
#     for valor in valores:
#         suma +=valor
#     return suma

# # hacer sumas
# # Puedo validar cosas

# def calcular_promedio(notas):
#     """Divide entre la cantidad de notas"""
#     return sumar_valores(notas) / len(notas)


# # calcular promedios
# # Puedo validar cosas

# print(calcular_promedio([8,8,9,10,6,7]))





"""
Las funciones se definen utilizando la palabra def,
luego se pone un nombre (con las mismas reglas que las variables)
Luego, dentro del cuerpo de la funcion,
debemos poner lo que hace.
y por ultimo, devolvemos el resultado usando la palabra clave return.
Podemos utilizar más de un return dentro de una función.
Se va va a ejecutar siempre un único return.
"""


def foo(a, b):
    """Lo explícito es mejor que lo implícito."""
    resultado = ""
    if a == 5:
        resultado = "a es 5."
    if b == 7:
        resultado = "b es 7."
    return resultado


print(foo(7, 2))


# def mi_funcion():
#     a = 5

# print(mi_funcion())



"""3. Realizar una función que reciba dos números y nos indique cual de los
números es el mayor."""


def obtener_mayor(num1, num2):
    if num1 > num2:
        return f"El numero {num1} es mayor a {num2}"
    elif num1 == num2:
        return f"Los numeros son iguales ({num1})"
    else:
        return f"El numero {num2} es mayor a {num1}"
    
print(obtener_mayor(1,2))
print(obtener_mayor(2,3))
print(obtener_mayor(2,2))