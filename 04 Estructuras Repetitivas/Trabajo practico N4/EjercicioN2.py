numero = input("Ingrese un numero entero: ") #Se una input para permitir numeros grandes

if numero.isdigit() or (numero[0] == '-' and numero[1:].isdigit()): #Valida numeros negativos
    cantidad_digitos = len(numero.lstrip('-'))
    print(f"El numero tiene {cantidad_digitos} digitos.")
else:
    print("Por favor, ingrese un numero entero valido.")