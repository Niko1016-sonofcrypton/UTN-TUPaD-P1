import random #Se importa el modulo para generar numeros aleatorios

#Generar un numero aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 0 #contador de intentos

print("Por favor adivina el numero entre el 1 y el 9")
while True:
    intento = int(input("Ingrese su numero: ")) #Solicitar intento al usuario
    intentos += 1 #sube la cantidad de intentos

    if intento == numero_secreto:
        print(f"Felicidades adivinaste el numero {numero_secreto} en {intentos} intentos!")
        break #se finaliza el juego al adivinar
    else:
        print("Intenta de nuevo.")