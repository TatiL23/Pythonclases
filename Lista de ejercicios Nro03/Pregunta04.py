class Catalogo:

    producto = []

    def __init__(self, producto = []):
        self.producto = producto

    def agregar(self, p):
        self.producto.append(p)

    def mostrar(self):
        for p in self.producto:
            print(p)  

c = Catalogo(["Llanta"]) 
c.agregar("Espejo")
c.mostrar()