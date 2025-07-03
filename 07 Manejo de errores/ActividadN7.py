#Se definen los sets de estudiantes que aprobaron cada parcial
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107}

#Calcular conjuntos 
ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

#Se muestran los resultados
print("Aprobaron ambos paciales: ", ambos)
print("Aprobaron solo uno: ", solo_uno)
print("Aprobaron al menos uno: ", al_menos_uno)
