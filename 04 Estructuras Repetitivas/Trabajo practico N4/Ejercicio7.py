#Se le solicita al usuario un numero
numero = int(input("Ingrese un numero entero positivo: "))

#Se verifica que el numero ingresado sea valido
if numero < 0:
    print("Por favor, ingrese un numero positivo.")
else:
    suma_total = sum(range(numero + 1)) #Se calcula la suma desde o hasta {numero}
    print(f"La suma de todos los numeros entre 0 y {numero} es: {suma_total}")