import csv
import operator
from collections import Counter

def listar_esp():
    juegos_gratis_esp = []
    with open('appstore_games.csv','r', encoding='UTF-8') as archivo:
        reader = csv.reader(archivo, delimiter = ',')
        reader.__next__() #ignoro encabezado
        for line in reader:
            if line[7] == '0': #la linea 7 es precio
                lista_lenguajes = line[12].replace(' ','').split(',') #linea 12 es lenguaje
                if 'ES' in lista_lenguajes:
                    juegos_gratis_esp.append(line[2]) #linea 2 es nombre
    return juegos_gratis_esp


def top_10():
    lista10 = []    
    with open('appstore_games.csv','r', encoding='UTF-8') as archivo:
        reader = csv.reader(archivo, delimiter = ',')
        reader.__next__()
        dic = {}
        for linea in reader:
            if linea[6] != '':
                dic[linea[4]] = int(linea[6]) #linea 4 = URL // linea 6 = rating
        dic = sorted(dic.items(), key=operator.itemgetter(1))   
    contador = 0
    for i in reversed(range(len(dic))):
        if contador == 10:
            break
        lista10.append(dic[i])
        contador += 1
    return lista10
        

        

print(listar_esp())
print('-' * 190)
print(top_10())