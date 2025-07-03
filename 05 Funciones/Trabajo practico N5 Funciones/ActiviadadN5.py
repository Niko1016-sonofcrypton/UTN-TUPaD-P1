#Funcion que transforma segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

#Programa principal
segundos_ingresados = float(input("Ingresa la cantidad de segundos: "))
horas = segundos_a_horas(segundos_ingresados)
print(f"Equivale a {horas: .2f} horas.")