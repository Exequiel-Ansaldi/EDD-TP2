class Persona:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __eq__(self, other):
        if not isinstance(other, Persona):
            return False
        return self.nombre == other.nombre
    
    def __str__(self):
        return f"{self.nombre}"

    def __repr__(self):
        return f"{self.nombre}" 