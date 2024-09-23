"""
Dado un precio de un producto y un porcentaje variable, nos devuelva
el precio aumentado en dicho porcentaje. Por ejemplo, si el valor es
$100 y aumenta en un 15% nos debería devolver $115
"""

def calcular_aumento_precio(precio_actual: int | float, aumento: int | float) -> float:
    nuevo_precio = precio_actual * (1 + aumento / 100)
    return nuevo_precio

print(calcular_aumento_precio(1000, 20))

"""
Dado el precio de los productos y un porcentaje variable, nos devuelva
los precios aumentados en dichos porcentajes.
"""

lista_precios = [1000, 3000, 5000.50, 6000.99, 9000, 123, 4565, 456]

def calcular_precios_aumentados(lista_precios: list[int] | list[float], aumento: int | float) -> list[float]:
    nueva_lista_precios = []
    for precio in lista_precios:
        nueva_lista_precios.append(calcular_aumento_precio(precio, aumento))
    return nueva_lista_precios


nueva_lista_precios = calcular_precios_aumentados(lista_precios=lista_precios, aumento=20)
print(nueva_lista_precios)


"""
Dado una lista de diccionarios con los productos y un porcentaje variable, nos devuelva
los precios aumentados en dichos porcentajes. Además se debe poder aumentar por tipo de producto
"""


productos = [
    {
        "codigo": 127836262,
        "tipo": "lacteo",
        "nombre": "Leche",
        "precio": 1500
    },
    {
        "codigo": 456454444,
        "tipo": "cereal",
        "nombre": "Avena",
        "precio": 800
    },
    {
        "codigo": 87898999,
        "tipo": "verdura",
        "nombre": "Lechuga",
        "precio": 4000
    }
]

aumentos = {
    "lacteo": 20,
    "cereal": 40,
    "verdura": 10
}

def calcular_precio_productos(productos: list[dict], aumentos: dict) -> list:
    for producto in productos:
        tipo_producto = producto['tipo']
        aumento = aumentos[tipo_producto]
        precio = producto['precio']
        producto['precio'] = calcular_aumento_precio(precio, aumento)
    return productos

print(calcular_precio_productos(productos, aumentos))

def calcular_precio_productos_refactor(productos: list[dict], aumentos: dict) -> list:
    for producto in productos:
        aumento = aumentos[producto['tipo']]
        producto['precio'] = calcular_aumento_precio(producto['precio'], aumento)
    return productos
print(calcular_precio_productos_refactor(productos, aumentos))


# https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
canasta_naranjas = []
cn = []

naranjas_buenas = [naranja for naranja in canasta_naranjas if naranja != 'podrida']
naranjas_buenas = [n for n in cn if n != 'podrida']
