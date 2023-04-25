
def dice(self):
    return "guauuu"

Animal = type("Animal", (), {"nombre": "a definir"})
Perro = type("Perro", (Animal, ), dict(cantidad_patas=4, dice=dice))

p = Perro()
# print(p.nombre)
# print(p.cantidad_patas)
# print(p.dice())

class Madre():
    def __init__(self, nombre, apellido, dni, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
    def hablar(self):
        return f"Hola! Soy {self.nombre}, tu madre!"
    def correr(self):
        return "Corriendo"

class Padre():
    def __init__(self, nombre, apellido, dni, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
    def hablar(self):
        return f"Hola! Soy {self.nombre}, tu padre!"
    def caminar(self):
        return "Caminando"
    
class Hijo(Padre, Madre): 
    def __init__(self, nombre, apellido, dni, edad):
        super().__init__(nombre, apellido, dni, edad)
        self.nombre = nombre
    def hablar(self):
        return Madre.hablar(self)
        
    # def hablar(self):
    #     Madre.hablar()
hijo = Hijo("Jorge", "Gomez", 1234, 12)

print(hijo.hablar())
