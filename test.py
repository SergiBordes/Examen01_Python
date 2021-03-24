# =====================
# Sergi Bordes Lloria
# 24 / 03 / 2021 
# Examen 01 - Python 
# =====================

import examen
from libro import Libro
from autor import Autor
import unittest

listaLibros = []
l1 = Libro("Sergi", "Lo que el viento se llevó", 1995)
listaLibros.append(l1)
l2 = Libro("Claudia", "Los pilares de la Tierra", 2002)
listaLibros.append(l2)
res = examen.mas_antiguos(listaLibros, 1999)
res2 = examen.mas_antiguos(listaLibros, 2003)


class Pruebas (unittest.TestCase):

    def test_1 (self):
        self.assertEqual(res[0], "Lo que el viento se llevó")

    def test_2 (self):
        self.assertEqual(len(res2), 2)














if __name__ == "__main__":
    unittest.main()
