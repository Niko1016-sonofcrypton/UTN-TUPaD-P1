#Le solicitamos la magnitud del terremoto al usuario
magnitud = float(input("Ingrese la magnitud del terremoto segun la escala de Richter: "))

#Se clasifica la magnitud
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños a estructuras debiles)")
elif 6 <= magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")