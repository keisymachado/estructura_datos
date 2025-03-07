class Cancion:
    def __init__(self, titulo: str, artista: str, album: str, duracion: str):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

    def reproducir(self):
        print(f"Reproduciendo '{self.titulo}' de {self.artista} (Álbum: {self.album}, Duración: {self.duracion}).")


cancion1 = Cancion("Bohemian Rhapsody", "Queen", "A Night at the Opera", "6:07")
cancion1.reproducir()