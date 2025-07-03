def es_palindromo(palabra):
    #Si la palabra tiene 1 o 0 caracteres, es polindromo
    if len(palabra) <= 1:
        return True
    #Si el primer y ultimo caracter no son iguales, no es palindromo
    if palabra[0]!= palabra[-1]:
        return False
    #Si son iguales, se llama la funcion recursivamente con los caracteres del medio
    return es_palindromo(palabra[1:-1])

#Se solicita la palabra al ususario
entrada = input("Ingresa una palabra sin espacios ni tildes: ").lower()

#Se verifica si es palindromo
resultado = es_palindromo(entrada)

#Se muestra el resultado
print(f"¿{entrada} es palindromo?: {resultado}")