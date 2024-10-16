class A:
    def __init__(self, a, b):
        print("Inicializando variables")
        self.a = a
        print(self.a)
        self.b = b
        print(self.b)

    def __new__(self, *args, **kwargs):
        print("Creando objeto")
        return super().__new__(self)
    
    def __del__(self):
        print("Eliminando objeto")


a = A(1,2)
del a