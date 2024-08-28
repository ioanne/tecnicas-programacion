"""
1. Creación de un diccionario numérico
Crear un diccionario llamado numeros donde la clave sea un número
entero y el valor asociado sea el mismo número pero decimal..
Documenta el código explicando la estructura del diccionario y cómo se
han asignado los valores.

"""

numeros = {
    1: 1.0,
    2: 2.0,
    3: 3.0
}

# Los diccionarios estan compuesta por clave / valor
# Las claves tienen que ser valores no mutables.
# Las claves deben ser numeros o caracteres de texto
# Si son caracteres de texto, lo recomendable es que sean de este formato
# clave_del_diccionario / clave




"""
2. Creación de un diccionario de textos
Crear un diccionario llamado texto donde la clave sea una cadena de
texto (string) y el valor asociado sea otra cadena de texto.
Documenta el código explicando cómo se han definido las claves y los
valores.

"""

texto = {
    "saludo": "Hola, como estas?",
    "nombre": "Juan",
    "apellido": "Perez",
    "1": 1.0
}

{} # Diccionario vacio
{
    "clave": "valor",
    "clave2": "valor2",
    "clave3": "valor3",
    "clave4": "valor4",
    "clave5": "valor5",
}



"""
3. Creación de un diccionario con listas
Crear un diccionario llamado listas donde la clave sea una cadena de
texto (string) y el valor asociado sea una lista de cadenas de texto.

"""

listas = {
    "nombre": "Juan",
    "direcciones": [
        "Avenida siempre viva 123",
        "Calle falsa 123",
    ]
}

"""
4. Anidación de un diccionario dentro de otro
Usando el diccionario creado en el ejercicio anterior, crea un nuevo
diccionario llamado diccionario_anidado donde la clave sea una cadena
de texto (string) y el valor asociado sea el diccionario listas.
Documenta y explica cómo se almacena un diccionario dentro de otro y
analiza el resultado.
"""

diccionario_anidado = {
    "personas": listas
}

diccionario_anidado = {
    "personas": {
        "nombre": "Juan",
        "direcciones": [
            "Avenida siempre viva 123",
            "Calle falsa 123",
        ]
    }
}



"""
5. Creación de un perfil de usuario con diccionarios anidados
Crear un diccionario llamado perfil_usuario que contenga otro
diccionario como valor. Este diccionario interno debe tener las siguientes
claves y valores: un número entero (id), una cadena de texto (nombre y
apellido), una lista de cadenas de texto (direcciones), y otro diccionario
que contenga información de contacto (telefono, celular, email, etc).
Documenta detalladamente cómo has estructurado el diccionario y
explica la organización de los datos dentro del mismo.
"""

perfil_usuario = {
    "perfil_1": {
        "id": 1,
        "nombre": "Juan",
        "apellido": "Perez",
        "direcciones": [
            "Avenida siempre viva 123",
            "Calle falsa 123"
        ],
        "contacto": {
            "telefono": 12312312,
            "celular": 12312312,
            "email": "juan.perez@gmail.com",
            "nacimiento": "01/01/1990"
        }
    }
}




"""
Crear una lista de compra
los cuales se accede a los clientes, direcciones, productos (precio), cantidad
"""

lista_compras = {
    "cliente": {
        "nombre": "Juan",
        "apellido": "Perez",
        "direcciones": [
            {
                "calle": "Avenida siempre viva, 123",
                "por_defecto": True
            }, {
                "calle": "Calle falsa 123",
                "por_defecto": False
            }
        ]
    },
    "productos": [
        {
            "nombre": "Jabon",
            "precio": 2000,
            "cantidad": 4
        }, {
            "nombre": "Shampoo",
            "precio": 9000,
            "cantidad": 1
        }
    ]
}



direcciones_cliente = [
    {
        "calle": "Avenida siempre viva, 123",
        "por_defecto": True
    }, {
        "calle": "Calle falsa 123",
        "por_defecto": False
    }
]

cliente = {
    "nombre": "Juan",
    "apellido": "Perez",
    "direcciones": direcciones_cliente
}

productos = [
        {
            "nombre": "Jabon",
            "precio": 2000,
            "cantidad": 4
        }, {
            "nombre": "Shampoo",
            "precio": 9000,
            "cantidad": 1
        }
]

lista_compras = {
    "cliente": cliente,
    "productos": productos 
}

