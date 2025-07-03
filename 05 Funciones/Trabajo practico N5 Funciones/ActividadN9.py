def celsius_a_fahrenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return round(farenheit, 2)

#Se solicita la temp al usuario

celsius = float(input("Ingrese la temperatura en grados celsius: "))

#usamos la funcion y nos muestra el resultado

resultado = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {resultado}°F")