"""Escribir un programa que pregunte por consola el precio 
de un producto en euros con dos decimales y muestre por 
pantalla el número de euros y el número de céntimos del 
precio introducido."""
while True:
    precio = input("Introduce precio con dos decimales: ")
    if "." in precio:
        precio2 = precio.split(".")
    elif "," in precio:
        precio2 = precio.split(",")
  
    uno = precio2[0]
    dos = precio2[1]
    print(uno,"euros y ",dos," centimos")
