#Definimos la funcion recusriva 
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

#Se solicita los datos al usuario 
base = int(input("Ingrese la base: "))
exponente =int(input("Ingrese el exponente (>= 0): "))

#Validamos rapido
if exponente < 0:
    print("Por ahora solo funciona con exponentes enteros positivos.")
else:
    resultado = potencia(base, exponente)
    print(f"{base}**{exponente} = {resultado}")
    