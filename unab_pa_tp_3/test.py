from cancion import Cancion
from libro import Libro
from linea import Linea
from punto import Punto

punto = Punto(1, 2)
punto2 = Punto(3, 4)
print(punto.impresion())
print(punto2.opuesto())
print(punto == punto2)
# ---------------------------
linea = Linea(punto, punto2)
print(linea.impresion())
linea.mueve_arriba(0.5)
print(linea.impresion())
# ---------------------------
cancion = Cancion("Canción", "Artista")
print(cancion.get_titulo())
print(cancion.get_autor())
cancion.set_autor("Artista 2")
print(cancion.get_autor())
# ---------------------------
libro = Libro("Introduction to Java Programming", "Liang, Y. Daniel", "0-13-031997-X", 784, "3a.", "Prentice-Hall", ["New Jersey", "USA"], "viernes 16 de noviembre de 2001")
# print(libro.get_titulo())
# print(libro.get_autor())
print(libro)