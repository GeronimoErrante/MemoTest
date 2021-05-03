import csv
import os
import json
import collections
import operator


def calcularLol():
    bans = []
    if os.path.exists('src/csv/bans.csv'): 
        with open('src/csv/bans.csv', 'r', encoding='UTF-8') as file_csv:
            reader = csv.DictReader(file_csv)
            for linea in reader:                          
                bans.append(linea['ban_1'])
                bans.append(linea['ban_2'])
                bans.append(linea['ban_3'])                  
                bans.append(linea['ban_4'])
                bans.append(linea['ban_5'])       
        bans = dict(collections.Counter(bans))
        bans = list(sorted(bans.items(), key=operator.itemgetter(1), reverse=True)) #ordeno por valor
        bans.pop(0) #borro los espacios
        bans = bans[:10] #me quedo con los 10 primeros
        if not os.path.exists('masBaneados'):
            with open('masBaneados.json', 'w') as file_json:
                file_json.write(json.dumps(bans, indent=2))

        