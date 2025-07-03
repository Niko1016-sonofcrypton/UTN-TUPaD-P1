def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
#Solicitamos el numero al usuario
n = int(input("Ingrese un numero entero positivo: "))
binario = decimal_a_binario(n)
print(f"{n} en binario es: {binario}")