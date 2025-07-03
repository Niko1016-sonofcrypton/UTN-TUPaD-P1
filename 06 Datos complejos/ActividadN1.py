def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
#Solicitamos el numero al usuario
limite = int(input("Ingrese un un numero entero mayor a 0: "))

#Se muestra factoriales desde 1 hasta el numero ingresado

for i in range (1, limite + 1):
    print(f"{i}! = {factorial(i)}")
    