"""Escribir un programa que pida al usuario que introduzca 
una frase en la consola y muestre por pantalla la frase 
invertida."""

frase=input("introduce frase")
lon = len(frase)
frase2=frase[-1:-lon-1:-1]
print(frase2)