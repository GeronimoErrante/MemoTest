import csv
import os
import json
import collections
import operator


def calcularArtistas():
    arts = []
    if os.path.exists('src/csv/top50.csv'):
        with open('src/csv/top50.csv', 'r') as file_csv:
            reader = csv.DictReader(file_csv)
            for linea in reader: 
                dic = {'Cancion':linea['Track.Name'],'Popularidad': int(linea['Popularity'])}                                     
                arts.append(dic)    
        arts = list(sorted(arts,key=lambda a:a['Popularidad'], reverse=True)) #ordeno por popularidad
        arts = arts[:10] #me quedo con los  10 primeros
        if not os.path.exists('masEscuchados.json'): #si no existe creo el archivo, si existe no hago nada
            with open('masEscuchados.json', 'w') as file_json:
                file_json.write(json.dumps(arts, indent=2))