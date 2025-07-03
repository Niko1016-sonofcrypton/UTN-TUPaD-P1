#Definicion de la funcion
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (Division por cero)"
    return (suma, resta, multiplicacion, division)

#Programa principal
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

resultados = operaciones_basicas(num1, num2)

#Mostrar resultados de forma clara
print("\nResultados: ")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"Division: {resultados[3]}")