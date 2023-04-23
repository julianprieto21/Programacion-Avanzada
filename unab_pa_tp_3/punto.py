class Punto():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def eje_x(self):
        return self.x
    def eje_y(self):
        return self.y
    def impresion(self):
        return (str(self.x) + ", " + str(self.y))
    def opuesto(self):
        return (-self.x, -self.y)
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def move_x(self, cantidad):
        self.x += cantidad
    def move_y(self, cantidad):
        self.y += cantidad