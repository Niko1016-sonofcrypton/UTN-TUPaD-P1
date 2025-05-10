#Se solicita la informacion del hemisferio, mes, dia
hemisferio = input("Ingrese su hemisferio (N/S): ").strip().upper()
mes = int(input("Ingrese el numero del mes (1-12): "))
dia = int(input("Ingrese el dia del mes: "))

#Se verifica la estacion del año segun el hemisferio
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion ="Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes ==12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio invalido. Por favor, ingrese N o S"
#Se imprime la estacion correspondiente
print(f"La estacion del año es: {estacion}")


