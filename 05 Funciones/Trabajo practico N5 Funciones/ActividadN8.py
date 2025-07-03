def calc_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2)
#Solicitar datos al usuario
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

#Se llama a la funcion y muestra el resultado

resultado = calc_imc(peso, altura)
print(f"Tu indice de masa corporal (IMC es: {resultado})")
