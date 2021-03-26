texto = "este es un texto comun y corriente"
letra = input("Ingrese una letra: ")
letra = letra.upper()
palabras = texto.upper().split(" ")
if (letra < "A" or letra > "Z"):
    print("ERROR: usted no ha ingresado una letra")
else: 
    for p in palabras:
        if (p.startswith(letra)):
            print(p)