msg = """Elija una de las siguientes opciones:

a) Dibujar un cuadrado
b) Verificar si el número es múltiplo de 2
c) Mostrar las personas mayores de edad
"""
print(msg)
numeroOne=int(input('ingrese un valor:'))
opcionMenu=input('ingrese la opcion del menu:').upper()
## Menu

print(numeroOne,opcionMenu)
j = 0
i = 0
if(opcionMenu!='A' or opcionMenu!='B' or opcionMenu!='C'):
    if opcionMenu=='A':
        j = 0
        i = 0
        while i<numeroOne:
            while j<numeroOne:
                print("*",end=" ")
                j+=1
            print("")
            i+=1
            j=0
    elif opcionMenu=='B':
        k=0
        numero=0
        numeros=[]
        while k<numeroOne:
            numero+=1
            if numero%2==0:
                numeros.append(numero)
            k+=1
        print("Los números múltiplos de 2 son: ",numeros)
    elif opcionMenu=='C':
        numeroOne=int(input('ingrese un valor:'))
        NomEda=[['alberto', '56'], ['bryan', '32'], ['carlos', '11'], ['dario', '55'],
        ['erick', '23'], ['fabricio', '12'], ['german', '21'], ['hugo', '18']]
        l=0
        Nombre=[]
        while(l<numeroOne):
            numero = int(NomEda[l][1])
            if numero>18:
                Nombre.append(NomEda[l][0])
            l+=1
        print("Los mayores de edad son: ",Nombre)
    else:
        print('esta opcion no es valida')
else:
    print('elija una opcion correcta')