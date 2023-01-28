from Pregunta05 import *
import os
from Pregunta05 import *

while(True):
    try:
        n = int(input("Introduce un número: "))
        i=1
        numeros = []
        while(i<=n):
            numeros.append(i)
            i+=1
        m = 6
        SumaNumeros(numeros)
        Division(n,m)
        break
    except:
        print("Ha ocurrido un error, ingrese un número")
    else:
        print("La ruta del directorio de trabajo es: ", os.getcwd())
        break
    finally:
        print("Proceso terminado")