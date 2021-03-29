#1: A, E, I, O, U, L, N, R, S, T 
#2: D, G  
#3: B, C, M, P 
#4: F, H, V, W, Y 
#5: K  
#6: J, X  
#7: Q, Z 


tabla = {
1:('A','E','I','O','U','L','N','R','S','T'),
2:('D','G'),
3:('B','C','M','P'),
4:('F','H','V','W','Y'),
5:('K', ),
8:('J','X'),
10:('Q','Z')
}

#lista con las claves del diccionario
#claves = list(tabla.keys())

palabra = input("Ingres palabra: ").upper()
p = [c for c in palabra if palabra.isalpha()]
pts = 0


#for c in p:   
#    for key in tabla: 
#         if c in tabla[key]:
#             pts = pts + key
#             break 

for c in p:
    for k,l in tabla.items():
        if c in l:
            pts = pts + k
            break

print("La plabra '"+palabra.capitalize()+f"' vale {pts} puntos"  )