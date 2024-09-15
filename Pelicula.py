from typing import List
import datetime
from Persona import Persona
from Genero import Genero
class Pelicula:
        def __init__(self, id: int, titulo: str, fecha_publicacion: datetime.date, retorno: int, duracion_minutos: int, presupuesto: float, sitio_web: str, idioma_original: str, poster: str, rating: float, famosos_list: List[Persona], generos_list: List[Genero], persona: Persona, genero: Genero):
                self.id = id
                self.titulo = titulo
                self.fecha_publicacion = fecha_publicacion
                self.retorno = retorno
                self.duracion_minutos = duracion_minutos
                self.presupuesto = presupuesto
                self.sitio_web= sitio_web
                self.idioma_original = idioma_original
                self.poster = poster
                self.rating = rating
                self.famosos_list = famosos_list
                self.generos_list = generos_list
                self.persona = persona
                self.genero = genero

        def __eq__(self, other):
                if not isinstance(other, Pelicula):
                        return NotImplemented
                return self.id == other.id

        def __str__(self):
                return (f"Pelicula (id={self.id}, titulo={self.titulo}, fecha_publicacion={self.fecha_publicacion}, "
                f"retorno={self.retorno}, presupuesto={self.presupuesto}, sitio_web={self.sitio_web}, "
                f"idioma_original={self.idioma_original}, poster={self.poster}, rating={self.rating}, "
                f"famosos_lista={self.famosos_list}, generos_lista={self.generos_list}, persona= {self.persona}, genero= {self.genero})")