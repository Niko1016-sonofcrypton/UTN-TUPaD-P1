#Se solicita al usuario una frase o palabra 
texto = input("Ingrese una frase o una palabra: ")

#Se verifica si el ultimo caracter es una vocal
if texto[-1].lower() in "aeiou":
    texto +="!" #Se agregar el signo de exclamacion si termina en vocal

    #Se imprime el resultado
print(texto)