import random
from statistics import mode, median, mean 

#Se genera la lista de numeros aleatorios
numeros_aleatorios = [random.randint(1,100) for _ in range(50)]

#Se calculan los parametros estadisticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
 
#Se determina el sesgo
if media > mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo"

#Imprimir resultados
print(f"Numeros aleatorios: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Tipo de sesgo: {sesgo}")
