from punto import Punto


class Linea():
    def __init__(self, p_1: Punto, p_2: Punto):
        self._punto_a = p_1
        self._punto_b = p_2
    def impresion(self):
        return (self._punto_a.impresion() + " - " + self._punto_b.impresion())
    def mueve_derecha(self, cantidad: float):
        self._punto_a.move_x(cantidad)
        self._punto_b.move_x(cantidad)
    def mueve_izquierda(self, cantidad: float):
        self._punto_a.move_x(-cantidad)
        self._punto_b.move_x(-cantidad)
    def mueve_arriba(self, cantidad: float):
        self._punto_a.move_y(cantidad)
        self._punto_b.move_y(cantidad)
    def mueve_abajo(self, cantidad: float):
        self._punto_a.move_y(-cantidad)
        self._punto_b.move_y(-cantidad)
      