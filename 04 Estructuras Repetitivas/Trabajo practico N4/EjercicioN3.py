#Solicitar los numeros al usuario
inicio = int(input("Ingrese el primer numero: "))
fin = int(input("Ingrese el segundo numero: "))

#Asegurarse que el 'Inicio sea menor que 'fin'
if inicio > fin:
    inicio, fin = fin, inicio 
#Se suman los numeros excluyendo los externos
suma = sum(range(inicio + 1, fin))
print(f"La suma de los numeros entre {inicio} y {fin} excluyendo los extremos, es {suma}")