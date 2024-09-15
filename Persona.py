class Persona:
    nombre=str

    def __init__(self,nombre: str):
        self.nombre = nombre


    def __eq__(self, other):
        if not isinstance(other, Persona):
            return NotImplemented
        return self.nombre == other.nombre
    
    def __str__(self):
        return f"Nombre de la persona: {self.nombre}"
