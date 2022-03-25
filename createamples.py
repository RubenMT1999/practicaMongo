from pymongo import MongoClient
from random import randint
from obtenerJSON import *


obtener_todas_url()
cargar_url()





#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient("mongodb+srv://RubenMT99:rubenn199900@cluster0.vvsry.mongodb.net/test?authSource=admin&replicaSet=atlas-9s6wyt-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")

db=client.peliculas
#Step 2: Create sample data




for x in range(len(miDiccionario['posiciones'])):
    peliculas = {
        'posicion' : miDiccionario['posiciones'][x],
        'titulo' : miDiccionario['titulos'][x],
        'anio' :    miDiccionario['anio'][x],
        'valoracion': miDiccionario['valoraciones'][x],
        'sinopsis': miDiccionario['sinopsis'][x],
        'imagen': miDiccionario['imagenes'][x],
    }


    #Step 3: Insert business object directly into MongoDB via insert_one
    result=db.peliculas.insert_one(peliculas)

#Step 5: Tell us that you are done
print('finished creating 500 business reviews')