#Se inicia el acumulador
suma_total = 0

#Pedir 100 numeros al usuario
for _ in range(100):
    numero = int(input("Ingrese un numero entero: "))
    suma_total += numero
    
    #Se calcula la media
    media = suma_total / 100
    
    #Mostrar el resultado
    print(f"La media de los 100 numeros ingresados es: {media}")