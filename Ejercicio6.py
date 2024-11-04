"""Escribir un programa que pida al usuario que introduzca 
una frase en la consola y una vocal, y después muestre por 
antalla la misma frase pero con la vocal introducida en 
mayúscula."""

frase = input("introduce frase\n")
vocal = input("introduce vocal en minuscula\n")
vocalMayus = vocal.upper()
vocalMinus = vocal.lower()
frase2 = frase.replace(vocalMinus,vocalMayus)

print(frase2)