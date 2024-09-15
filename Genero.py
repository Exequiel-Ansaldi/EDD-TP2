class Genero:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __eq__(self, other):
        if not isinstance(other, Genero):
            return NotImplemented
        return self.nombre == other.nombre

    def __str__(self):
        return f"Nombre del genero: {self.nombre}"