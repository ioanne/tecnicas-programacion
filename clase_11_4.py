class B:
    def __init__(self) -> None:
        print("Creando la clase B")

class A:
    def __init__(self, a, b):
        print("Inicializando variables")
        self.a = a
        print(self.a)
        self.b = b
        print(self.b)

    def __new__(self, *args, **kwargs):
        print("Creando objeto")
        return B()
    
    def __del__(self):
        print("Eliminando objeto")


a = A(1,2)
print(a)


a = A()
b = B()

a + b