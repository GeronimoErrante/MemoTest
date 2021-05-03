import Estructuras as est
#Opcion 1
def cargar_estructura(list_alum):
    #vars
    nom = est.nombre
    n1 = est.eva1
    n2 = est.eva2
    #codigo
    def crear_dic(n):
        dic = dict(nombre = nom[n].capitalize(), nota_1 = int(n1[n]), nota_2 = int(n2[n]),
                   nota_final = int(n1[n]) + int(n2[n]))
        return dic
    list_alum = [crear_dic(n) for n in range(len(est.nombre))]
    return list_alum

def prom_gral(list_alum):
    "Retorna una cadena con la suma y el promedio general de las notas"
    suma = (sum(alum.get('nota_final') for alum in list_alum))
    promedio = suma / len(list_alum)
    cadena = f"Suma nota finales = {suma}  /  Promedio general = {round(promedio,2)}"
    return cadena

#Opcion 2
def definir_clave(opc):
    if opc == 'a':
        n = 'nota_1'
    elif opc == 'b':
        n = 'nota_2'
    else:
        n = 'nota_final'
    return n

def definir_rango(opc):
    ok = False
    if opc in ['a','b']:
        r = range(1,100)
        ok = True
    elif opc == 'c':
        r = range(1,200)
        ok = True
    if ok:
        r_min = int(input('Ingrese rango minimo: '))
        if r_min in r:
            r_max = int(input('Ingrese rango maximo: '))
            if r_max in r and r_max > r_min:
                return range(r_min,r_max)  
    return False

def lista_filter(nota,rango,*args):
    lista_n = list(filter(lambda dic: dic[nota] in rango ,args[0]))
    return lista_n


#Imprimir Estructuras
def print_info(list_alum):
    f = ('{:10} {:10} {:10} {:10}')
    f_dos = ('{:10} {:5} {:10} {:10}')
    linea = '- ' * 22
    print(f.format('Nombre','Nota 1','Nota 2','Nota Final'))
    print(linea)
    for a in list_alum:
        print(f_dos.format(a['nombre'],a['nota_1'],a['nota_2'],a['nota_final']))
    print(linea)