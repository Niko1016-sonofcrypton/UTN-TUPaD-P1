#Definimos la funcion que nos devuelve un saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
#Iniciamos el programa principal
nombre_ingresado = input("¿Cual es tu nombre? ")
saludo = saludar_usuario(nombre_ingresado)
print(saludo)