"""Escribir un programa que pregunte el 
nombre de un producto, su precio y un 
número de unidades y muestre por pantalla 
una cadena con el nombre del producto seguido 
de su precio unitario con 6 dígitos enteros 
y 2 decimales, el número de unidades con tres 
dígitos y el coste total con 8 dígitos enteros 
y 2 decimales."""
while True:
    prod = input("introduce nombre producto: ")
    prec = input("introduce precio: ")
    unid = int(input("intorduce unidades: "))


    prec = prec.replace(",",".")
    prec = round(float(prec),2)

    total = prec * unid

    prec = "{:09.2f}".format(prec)

    unid = "{:>03}".format(unid)
    
    total = "{:011.2f}".format(total)
    
    print("producto:",prod+"\nPrecio unidad:",prec+"\nCantidad:",unid+"\nPrecio total:",total)