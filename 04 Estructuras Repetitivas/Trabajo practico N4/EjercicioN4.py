#Inicializar la variable acumulacion
total = 0
while True : #bucle infinito con determinacion interna
    numero = int(input("Ingrese un numero entero entre (0 para finalizar): "))
    if numero == 0: #Si el usuario ingresa 0 el bucle se detiene
        break
    total += numero #Se acumula la suma
print(f"La suma total de los numeros ingresados es {total}")