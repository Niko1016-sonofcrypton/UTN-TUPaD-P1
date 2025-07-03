def contar_digito(numero,digito):
    #Si el numero ya se redujo a cero, termina la recursion
    if numero == 0: 
        return 0
    else:
        #Compara el ultimo digito con el buscado
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
        
#El usuario ingresa
numero = int(input("Ingresa un numero entero positivo: "))
digito = int(input("Ingresa el digito que queres contar (entre 0 y 9): "))

#Vlidacion 
if numero < 0 or digito < 0 or digito > 9:
    print("Por favor ingresa valores validos.")
else:
    resultado = contar_digito(numero, digito)
    print(f"El digito {digito} aparece {resultado} veces en el numero {numero}.")
