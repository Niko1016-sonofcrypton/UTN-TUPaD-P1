#Se le solicita al usuario que ingrese un numero
numero = int(input("Ingrese un numero: "))

#Se verifica si el numero es par si no es aparece en pantalla un mensaje diciendo por favor ingrese un numero par
if numero % 2 == 0:
    print(" Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")