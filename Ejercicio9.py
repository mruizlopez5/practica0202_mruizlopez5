"""Escribir un programa que pregunte al usuario la fecha de 
su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
el día, el mes y el año. Adaptar el programa anterior para 
que también funcione cuando el día o el mes se introduzcan 
con un solo carácter."""

fecha = input("introduce tu fecha de nacimiento en formato dd/mm/aa\n")
fecha = fecha.split("/")
print("dia: ",fecha[0],"\nmes: ",fecha[1],"\naño:",fecha[2])