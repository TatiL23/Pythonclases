def Separar(tex):
    txt = tex.split()
    print(txt)

def Unir(tex):
    txt = "/".join(tex)
    print(txt)

def Contar(tex,palabra):
    txt = tex.count(palabra)
    print(txt)

def Encontrar(tex,palabra):
    txt = tex.find(palabra)
    print(txt)

def ConvMayus(tex):
    txt = tex.upper()
    print(txt)

def ConvMinus(tex):
    txt = tex.lower()
    print(txt)

texto = """Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
Lorem ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galerías de textos
y los mezcló de tal manera que logró hacer un libro de textos especimen."""

Separar(texto)
Unir(texto)
Contar(texto,"texto")
Encontrar(texto,"persona")
ConvMayus(texto)
ConvMinus(texto)