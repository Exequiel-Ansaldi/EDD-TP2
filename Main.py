from MamboretaAdmin import MamboretaAdmin
from typing import List
from Persona import Persona
from Genero import Genero
def main():
    admin = MamboretaAdmin()
    archivo_csv = r"C:\Users\GAMER\Documents\Algoritmos poo\Estructura\tp2\imdb.csv"
    admin.procesar_archivo(archivo_csv)
    print(admin)

if __name__ == "__main__":
    main()






