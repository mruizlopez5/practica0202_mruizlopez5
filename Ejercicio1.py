"""Escribir un programa que pregunte el nombre del usuario 
en la consola y un número entero e imprima por pantalla en 
líneas distintas el nombre del usuario tantas veces como el 
número introducido."""

nombre = input("intriduce nombre\n")
N = int(input("introduce veces\n"))
for i in range(N-1):
    print(nombre)


