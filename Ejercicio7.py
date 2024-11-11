"""Escribir un programa que pregunte el correo electrónico 
del usuario en la consola y muestre por pantalla otro correo 
electrónico con el mismo nombre (la parte delantera de la 
arroba @) pero con dominio ceu.es."""


while True:
    correo = input("Introduce correo electrónico: ")
    if "@" in correo: 
        correo2 = correo.split("@")
        correofnl = correo2[0] + "@ceu.es"
        print(correofnl)
    else:
        print("El correo debe contener @, introduce otra vez")