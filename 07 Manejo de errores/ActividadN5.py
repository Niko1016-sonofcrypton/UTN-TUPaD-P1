#Se solicita una oracion al usuario
oracion = input("Ingrese una oracion: ")
#Separar en palabras
palabras = oracion.split()
#Crear conjunto de palabras unicas
palabras_unicas = set(palabras)
#crear diccionario de recuento
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
#Mostramos el resultado
print("Palabras unicas: ", palabras_unicas)
print("Recuento: ", recuento)