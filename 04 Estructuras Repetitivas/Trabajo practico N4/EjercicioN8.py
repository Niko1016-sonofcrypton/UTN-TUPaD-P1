#Se inician los contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

#Se le pide al usuario los 100 numeros
for _ in range(100):
    numero = int(input("Ingrese un numero entero: "))
    #Se verifica si es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
        #Verificar si es positico o negativo
        if numero > 0:
            positivos += 1
        elif numero < 0:
            #Se muestran los resultados
            print("\nResultados:")

print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")