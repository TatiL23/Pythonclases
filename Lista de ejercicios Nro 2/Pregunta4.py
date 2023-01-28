import sys
def argumentos(*args):
    for arg in args:
        print("Los argumentos son",arg)
        

argumentos(sys.argv)
