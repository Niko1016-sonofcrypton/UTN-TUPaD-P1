#Definimos la funcion recursiva
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else: 
        return fibonacci(pos - 1) + fibonacci(pos - 2)

#Solicitamos al usuario la posicion limite
limite = int(input("Ingrese la cantidad de terminos de la serie Fibonacci: "))

#Se imprime la serie completa
print(f"Serie de fibonacci hasta la posicion {limite}: ")
for i in range (limite):
    print(fibonacci(i), end=" ")
    
