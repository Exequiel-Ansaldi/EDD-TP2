from abc import ABC, abstractmethod
from typing import List
from Pelicula import Pelicula
from Persona import Persona
from Genero import Genero

class MamboretaAdminAbstract(ABC):
    """
    Clase abstracta que define la estructura básica para un administrador de películas. 
    Permitiendo filtrar y organizar las mismas según diferentes criterios.
    """

    def __init__(self) -> None:
        """
        Inicializa una nueva instancia.
        """
        self.lista : List[Pelicula] = []

    @abstractmethod
    def procesar_archivo(self, ruta : str) -> None:
        """
        Añade todas las películas desde el archivo CSV cuya ruta se pasa como parámetro.

        Args:
            ruta (str): ruta hacia el archivo que se desea importar.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Concatena todas los elementos de lista en un único str.

        Returns:
            str: Una cadena que representa el objeto.
        """
        pass

    @abstractmethod
    def filtrar_por_genero(self, genero: Genero) -> List[Pelicula]:
        """
        Filtra las películas en la lista según el género especificado.

        Args:
            genero (Genero): El género por el cual se filtrarán las películas.

        Returns:
            List[Pelicula]: Una lista de películas que pertenecen al género especificado.
        """
        pass

    @abstractmethod
    def filtrar_por_persona(self, persona: Persona) -> List[Pelicula]:
        """
        Filtra las películas en la lista según un actor específico

        Args:
            persona (Persona): La persona por la cual se filtrarán las películas.

        Returns:
            List[Pelicula]: Una lista de películas asociadas con la persona especificada.
        """
        pass

    @abstractmethod
    def filtrar_companieros(self, persona1: Persona, persona2: Persona) -> List[Pelicula]:
        """
        Filtra las películas en las que dos personas específicas han trabajado juntas.

        Args:
            persona1 (Persona): La primera persona.
            persona2 (Persona): La segunda persona.

        Returns:
            List[Pelicula]: Una lista de películas en las que ambas personas han colaborado.
        """
        pass

    @abstractmethod
    def top_n(self, n: int = 50) -> List[Pelicula]:
        """
        Devuelve en orden descendente de rating las 'n' películas más destacadas

        Args:
            n (int): El número de películas a devolver.

        Returns:
            List[Pelicula]: Una lista con las 'n' mejores películas.
        """
        pass

    @abstractmethod
    def fracasos_comerciales(self, umbral: float = 0.0) -> List[Pelicula]:
        """
        Filtra y devuelve las películas que han sido fracasos comerciales.
        Por defecto, el umbral es 0.0, lo que significa que se considerará fracaso 
        cualquier película cuyo retorno sea menor que su presupuesto.

        Args:
            umbral (float, optional): El umbral para determinar el fracaso comercial. 
                                  Si la diferencia entre retorno y presupuesto es menor 
                                  que este valor, la película se considera un fracaso. 
                                  El valor predeterminado es 0.0.

        Returns:
            List[Pelicula]: Una lista de películas que no tuvieron éxito comercial.
        """
        pass
