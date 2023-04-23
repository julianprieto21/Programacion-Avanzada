class Persona():
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

class Libro():
    def __init__(self, titulo: str, autor: Persona, isbn: str, paginas: int, edicion: str, editorial: str, lugar: list[str, str], fecha_edicion: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_isbn(self):
        return self.isbn
    def get_paginas(self):
        return self.paginas
    def get_edicion(self):
        return self.edicion + " edición"
    def get_editorial(self):
        return self.editorial
    def get_lugar(self):
        return (self.lugar[0] + ", " + self.lugar[1])
    def get_fecha_edicion(self):
        return self.fecha_edicion
    def set_titulo(self, new_titulo: str):
        self.titulo = new_titulo
    def set_autor(self, new_autor: Persona):
        self.autor = new_autor
    def set_isbn(self, new_isbn: str):
        self.isbn = new_isbn
    def set_paginas(self, new_paginas: int):
        self.paginas = new_paginas
    def set_edicion(self, new_edicion: int):
        self.edicion = new_edicion
    def set_editorial(self, new_editorial: str):
        self.editorial = new_editorial
    def set_lugar(self, new_lugar: list[str, str]):
        self.lugar = new_lugar
    def set_fecha_edicion(self, new_fecha_edicion: str):
        self.fecha_edicion = new_fecha_edicion
    def __str__(self):
        return f"""
Título: {self.titulo} {self.edicion} edición
Autor: {self.autor}
ISBN: {self.isbn}
{self.editorial}, {self.lugar[0]} ({self.lugar[1]})
{self.fecha_edicion}
{self.paginas} páginas"""
    
    