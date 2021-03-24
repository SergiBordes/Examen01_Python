# =====================
# Sergi Bordes Lloria
# 24 / 03 / 2021 
# Examen 01 - Python 
# =====================

class Libro:

    def __init__(self, autor, titulo, anyo):
        self.__autor = autor
        self.__titulo = titulo
        self.__anyo = anyo


    def get_autor(self):
        return self.__autor

    def get_anyo(self):
        return int(self.__anyo)

    def get_titulo(self):
        return self.__titulo



# ====== MAIN ======