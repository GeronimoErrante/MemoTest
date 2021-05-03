#Imports
import Cadenas as cad
import Funciones as Func

#Funciones
def select_opc(msj):
    opc = input(msj)
    return opc

def opt_uno():
    """Crea una lista de diccionarios(cada alumno), calcula la suma
       de notas individuales,suma total de notas finales y promedio. 
       Luego imprime en pantalla.
    """
    #Funciones opcion 1
    global l_alum
    l_alum = Func.cargar_estructura(list) # crear lista diccionarios = OK
    Func.print_info(l_alum) #imprimir lista de diccionarios = OK
    print(Func.prom_gral(l_alum)) # imprimir suma notas finales y prom gral = OK

def opt_dos():
    """Muestra los valores dentro de un rango seleccionado de 'X' valor."""
    opc = select_opc(cad.submenu_a).lower()
    while opc != 'd':
        if opc in ['a','b','c']:
            #funciones opcion 2
            nota = Func.definir_clave(opc) #definir key segun char ingresado = OK
            rango = Func.definir_rango(opc) #definir rango valido = OK
            if not rango:
                print(cad.error)
            else:
                Func.print_info(Func.lista_filter(nota,rango,l_alum)) #Crear filter e imprimir = OK
        opc = select_opc(cad.submenu_a).lower()

def opt_tres():
    """Ordena los datos por el tipo de valor seleccionado y los imprime."""
    opc = input(cad.submenu_b).lower()
    while opc != 'e':
        if opc in ['a','b','c','d']:
            #funciones opcion 3
            return
        opc = input(cad.submenu_b).lower()
        
#Menu principal
def Menu():
    """Menu principal que da a elegir entre diferentes operaciones."""
    opc = int(select_opc(cad.menu_principal))
    open = False #Para comprobar si se ingreso la opcion 1
    while opc != 0:
        if opc in [1,2,3]:
            if opc == 1:
                opt_uno()
                open = True
            elif open:
                if opc == 2:
                    opt_dos()
                elif opc == 3:
                    opt_tres()
        if not open: print(cad.exc)
        opc = int(select_opc(cad.menu_principal))

#variables globales
l_alum = []

#Invocaciones
Menu()