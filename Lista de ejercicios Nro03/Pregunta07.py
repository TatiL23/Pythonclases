class Producto:
    def __init__(self, nombre, codigo:str):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self) -> str:
        return f"El código del {self.nombre} es: {self.codigo}"
        
    def Cod(self):
        a = self.codigo.split(sep='-')
        print(f"El país de origen es {a[0]} y el número de lote es {a[1]}")


c = Producto("VMX200","PERÚ-0204-2023")
print(c)
c.Cod()