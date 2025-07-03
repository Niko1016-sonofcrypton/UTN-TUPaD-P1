def calcular_promedio(a, b, c):
    promedio = (a + b+ c) / 3
    return round(promedio,2)

#Solicitamos los numeros al usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

#Se llama a la funcion y muestra el resultado

resultado = calcular_promedio(a, b, c)
print(f"El promedio de los tres numeros es: {resultado}")