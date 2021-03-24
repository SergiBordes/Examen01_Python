# =====================
# Sergi Bordes Lloria
# 24 / 03 / 2021 
# Examen 01 - Python 
# =====================

def get_list(fichero):
    dic={} #Creamos el diccionario donde almacenar las palabras
    #Abrimos el fichero en modo lectura:
    f = open(fichero, mode="rt", encoding="utf-8")

    for linea in f:
        palabras = linea.split()
        for i in range(0, len(palabras)):
            dic[len(palabras[i])] = palabras[i]

    return dic



# ====== MAIN ======
print(get_list("palabras.txt"))