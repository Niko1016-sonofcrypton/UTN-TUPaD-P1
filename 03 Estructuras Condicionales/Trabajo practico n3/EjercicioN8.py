#Solicita el nombre del usuario
nombre = input("Ingrese su nombre: ")

#Se solicita la opcion que el usuario desee
print("Elija una opcion: ")
print("1. Convertir a mayusculas")
print("2. Convertir a minusculas")
print("3. Convertir con la primera letra en mayuscula")
opcion = int(input("Ingrese el numero de la opcion deseada 1, 2 o 3: "))

#Transformar el nombre segun la opcion elegida
if opcion == 1:
    print("Nombre en mayusculas: ", nombre.upper())
elif opcion == 2:
    print("Nombre en minusculas: ", nombre.lower())
elif opcion == 3:
    print("Nombre con la primera letra en mayuscula: ", nombre.title()) 
else:
    print("Opcion invalida, intentelo de nuevo ingresando una de las opciones 1, 2 o 3")