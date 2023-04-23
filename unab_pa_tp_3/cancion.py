

class Cancion():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def set_titulo(self, new_titulo: str):
        self.titulo = new_titulo
    def set_autor(self, new_autor: str):
        self.autor = new_autor