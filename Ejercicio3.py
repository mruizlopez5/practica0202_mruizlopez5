"""Escribir un programa que pregunte el nombre del usuario 
en la consola y después de que el usuario lo introduzca 
muestre por pantalla <NOMBRE> tiene <n> letras, donde 
<NOMBRE> es el nombre de usuario en mayúsculas y <n> es el
 número de letras que tienen el nombre."""

name = input("introduce nombre\n")
lista=name.split(" ")



total = 0
N = len(lista)
for N in lista:
    total = total + len(N)

print(name,"tiene ",total," letras")


#otra forma 
name2=name.replace(" ","")
total2=len(name2)
print(name,"tiene ",total2," letras")