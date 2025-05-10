#Se solicita el numero al usuario
numero = input("Ingrese un numero entero: ")

#Se invierte el orden de los digitos
numero_invertido = numero[ ::-1 ] #Se usa slicing para invertir la cadena

#Mostrar el numero
print(f"El numero invertido es: {numero_invertido}")