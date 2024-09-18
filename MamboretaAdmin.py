import pandas as pd
from typing import List
from Pelicula import Pelicula
from Persona import Persona
from Genero import Genero
from mamboreta_admin_abstract import MamboretaAdminAbstract

class MamboretaAdmin(MamboretaAdminAbstract):
    def __init__(self) -> None:
        self.lista: List[Pelicula] = []

    def procesar_archivo(self, ruta: str) -> None:
        try:
            datos = pd.read_csv(ruta)
            for index, fila in datos.iterrows():
                try:
                    pelicula = Pelicula(
                        int(fila['id']),
                        str(fila['title']),
                        pd.to_datetime(fila['release_date']),
                        float(fila['revenue']),
                        int(fila['runtime']),
                        float(fila['budget']),
                        str(fila['homepage']),
                        str(fila['original_language']),
                        str(fila['Poster_Link']),
                        float(fila['IMDB_Rating']),
                        [Persona(nombre) for nombre in fila[['Star1', 'Star2', 'Star3', 'Star4']] if isinstance(nombre, str)],
                        [Genero(genero.strip("[]'")) for genero in fila.get('genres_list', '').split(', ')]
                        # [Genero(nombre.strip().replace('[', '').replace(']', '')) for nombre in fila['genres_list'].split(',') if nombre.strip()]
                        )
                    self.lista.append(pelicula)
                   

                except ValueError as e:
                    print(f"Error de valor en la fila {fila}: {e}")
                except Exception as e:
                    print(f"Ocurrió un error al procesar la fila {fila}: {e}")

        except FileNotFoundError:
            print(f"El archivo {ruta} no se encuentra.")
        except pd.errors.EmptyDataError:
            print("El archivo CSV está vacío.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def __str__(self) -> str:
        resultado = '\n'.join([str(pelicula) for pelicula in self.lista])
        return resultado

    def filtrar_por_genero(self, genero: Genero) -> List[Pelicula]:
        peliculas_por_genero = []
        for pelicula in self.lista:
            if genero in pelicula.generos_list:
                peliculas_por_genero.append(pelicula)            
        return peliculas_por_genero

    def filtrar_por_persona(self, persona: Persona) -> List[Pelicula]:
        peliculas_por_persona = []
        for pelicula in self.lista:
            famosos_list = pelicula.famosos_list
            if persona.nombre in [persona.nombre for persona in pelicula.famosos_list]:
                peliculas_por_persona.append(pelicula)
        return peliculas_por_persona

    def filtrar_companieros(self, persona1: Persona, persona2: Persona) -> List[Pelicula]:
        peliculas_companieros = []
        for pelicula in self.lista:
            famosos_list = pelicula.famosos_list
            if persona1 in famosos_list and persona2 in famosos_list:
                peliculas_companieros.append(pelicula)
        return peliculas_companieros
    
    def top_n(self, n: int = 50) -> List[Pelicula]:
        peliculas_ordenadas = sorted(self.lista, key=lambda pelicula: pelicula.rating, reverse=True)
        top_peliculas = peliculas_ordenadas[:n]
        return top_peliculas
    
    def fracasos_comerciales(self, umbral: float = 0.0) -> List[Pelicula]:
        fracasos = []
        for pelicula in self.lista:
            if (pelicula.retorno - pelicula.presupuesto) < umbral:
                fracasos.append(pelicula)
        return fracasos
                