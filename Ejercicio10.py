"""Escribir un programa que pregunte por consola por los productos de 
una cesta de la compra, separados por comas, y muestre por pantalla 
cada uno de los productos en una línea distinta. """

lista = input("intoduce lista de la compra separada por coma: ")
lista = lista.split(",")
N = int(len(lista))
for i in range(N):
    print(lista[i])