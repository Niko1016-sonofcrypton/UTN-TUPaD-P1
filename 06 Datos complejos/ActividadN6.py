def suma_digitos(n):
    #si el numero es de un solo digito, se devuelve tal cual
    if n < 10:
        return n
    else:
    #suma el ultimo digito con lo que devuelva la funcion para el resto
        return (n % 10) + suma_digitos(n // 10)
#Se solicita el numero al ususario
numero = int(input("Ingresa un número entero positivo: "))
#Se evitan negartivos
if numero < 0:
    print("Solo se aceptan numeros enteros positivos.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los digitos de {numero} es: {resultado}")
