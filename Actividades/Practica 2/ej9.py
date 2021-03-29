palabra = input("Ingrese una palabra para identificar si es un heterograma: ").lower()
p = palabra.replace(' ','')

car = [c for c in p if c.isalpha()]
car_unicos = list(set(car))
if(len(car) == len(car_unicos)):
    print("La palabra o frase '" + palabra.capitalize() + "' es un heterograma")
else:
    print("La palabra o frase ingresada no es un heterograma")