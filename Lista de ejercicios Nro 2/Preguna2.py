biblioteca = {
    'Categorias':["Ciencia Ficción","Cómics","Científicos","Suspenso","Videojuegos","Aventura","Cuentos"],
    'Nombres':{"Libros":["Dune","The legend of Zelda","La vida secreta de la mente","Miss Marte","LA leyenda de Zelda","La sangre de los inocentes","El hombre que vendió su ferrari"],
                "Autores":["Frank Herbert","Hyrule Historia","Mariano Sigman","Manuel Jabois","Enciclopedia","Julia Navarro","Robin Sharma"],
                },
    "Disponibilidad":{"1":"Disponible",
                "2":"Prestado",
                },
    "Usuarios":{"nombre":["Juan","Miguel","Roberta","Alberto","Gilberta","Leticia","Maya","Enrique"],
                "apellido":["Rodriguez","Lopez","Chipana","Alvarez","Altamirano","Osis","Yañez","Zapana"],
                },
}

msg = """Elija una de las siguientes opciones:

a) Ver categorías
b) Ver libros y autores
c) Cambiar disponibilidad del libro
d) Ver los usuarios
"""
print(msg)
opcionMenu=input('Ingrese la opcion del menu:').upper()

Categorias=biblioteca["Categorias"]
LibyAut=biblioteca["Nombres"]
Usuarios=biblioteca["Usuarios"]
if(opcionMenu!='A' or opcionMenu!='B' or opcionMenu!='C'):
    if opcionMenu=='A':
        print("Las categorías son: ",Categorias)
    if opcionMenu=='B':
            print("Los autores y libros son: ",LibyAut)
    if opcionMenu=='C':
        print("Escoja 1 para cambiar el libro como disponible y 2 para cambiar el libro como prestado")
        num=int(input("Número a escoger: "))
        if num==1:
            print("Libro disponible")
        elif num==2:
            print("Libro prestado")
        else:
            print("Dato incorrecto")
    if opcionMenu=='D':
            print("Los usuarios son: ",Usuarios)
    
    else:
        print('esta opcion no es valida')
else:
    print('elija una opcion correcta')