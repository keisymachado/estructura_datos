class Libro:
    def __init__(self, titulo: str, autor: str, genero: str, año_publicacion: int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año_publicacion = año_publicacion

    def mostrar_detalles(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año: {self.año_publicacion}")


libro1 = Libro("imperio final", "brandon sanderson", "Novela", 2010)
libro1.mostrar_detalles()