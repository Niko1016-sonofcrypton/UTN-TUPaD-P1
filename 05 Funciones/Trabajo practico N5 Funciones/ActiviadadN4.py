import math

#Funcion que va a calcular el area del circulo
def calcular_area_circulo(radio):
    return math.pi *radio ** 2

#Funcion que va a calcular el perimetro del circulo
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#Programa principal
radio_ingresado = float(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio_ingresado)
perimetro = calcular_perimetro_circulo(radio_ingresado)
print(f"\nArea del circulo: {area: .2f}")
print(f"Perimetro del circulo: {perimetro: .2f}")