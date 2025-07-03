def contar_bloques(n):
    #Si hay un bloque en el nivel mas alto no se puede reducir mas
    if n == 1: 
        return 1
    else:
        #Se suma el nivel actual con los niveles superiores
        return n + contar_bloques(n - 1)
    
#Se solicita al usuario el numero de bloques en el nivel mas bajo
nivel_inferior = int(input("Ingresa la cantidad de bloques en el nivel mas bajo de la piramide: "))

#Validacion opcional
if nivel_inferior < 1:
    print("El numero debe ser entero positivo mayor o igual a 1.")
else:
    total = contar_bloques(nivel_inferior)
    print(f"Se necesitan {total} bloques para construir la piramide completa.")
    