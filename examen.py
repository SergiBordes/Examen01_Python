# =====================
# Sergi Bordes Lloria
# 24 / 03 / 2021 
# Examen 01 - Python 
# =====================

from libro import Libro
from autor import Autor

def get_list(fichero):
    dic={} #Creamos el diccionario donde almacenar las palabras
    #Abrimos el fichero en modo lectura:
    f = open(fichero, mode="rt", encoding="utf-8")

    for linea in f:
        palabras = linea.split()
        for i in range(0, len(palabras)):
            dic[len(palabras[i])] = palabras[i]

    return dic



def mas_antiguos(libros, anyo):

    if anyo<1900 or anyo>2021:
        raise ValueError("El anyo debe ser mayor que 1900 y meonr or que 2021")

    listaFinal = []
    for i in range(len(libros)):
        if libros[i].get_anyo() < anyo:
            listaFinal.append(libros[i].get_titulo())

    return listaFinal





# ====== MAIN ======
#print(get_list("palabras.txt"))

listaLibros = []
l1 = Libro("Sergi", "Lo que el viento se llevó", 1995)
listaLibros.append(l1)
l2 = Libro("Claudia", "Los pilares de la Tierra", 2002)
listaLibros.append(l2)
res = mas_antiguos(listaLibros, 1999)
print(res)