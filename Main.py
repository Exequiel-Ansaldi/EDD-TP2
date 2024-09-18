from MamboretaAdmin import MamboretaAdmin
from typing import List
from Persona import Persona
from Genero import Genero


admin = MamboretaAdmin()
archivo_csv = 'imdb.csv'
admin.procesar_archivo(archivo_csv)


# print(admin)      
 

# persona = Persona('Chris Pratt')
# listaPersona = admin.filtrar_por_persona(persona) 
# for pelicula in listaPersona:
#     print(pelicula)

# p1 = Persona('Chris Pratt')
# p2 = Persona('Vin Diesel')
# Pelicula_Companiero = admin.filtrar_companieros(p1,p2)
# for pelicula in Pelicula_Companiero:
#     print(pelicula)

# genero = Genero('Crime')
# listaGeneroFilt = admin.filtrar_por_genero(genero)
# for pelicula in listaGeneroFilt:
#     print(pelicula)

# n = 2
# peliculaOrdenada = admin.top_n(n)
# for pelicula in peliculaOrdenada:
#     print(pelicula)

# listaFracaso = admin.fracasos_comerciales()
# for pelicula in listaFracaso:
#     print(pelicula)








