#Definimos la funcion
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Programa principal
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingrese tu edad: ")
residencia = input("Ingresa donde vivis: ")

#Se llama la funcion
informacion_personal(nombre, apellido, edad, residencia)