#Creamos diccionario vacio
alumnos = {}

#Ingresamos datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresa el nombre del alumno {i + 1}: ")
    nota1 = float(input(f"Ingresa la nota 1 de {nombre}: "))
    nota2 = float(input(f"Ingresa la nota 2 de {nombre}: "))
    nota3 = float(input(f"Ingresa la nota 3 de {nombre}: "))
    alumnos[nombre] = (nota1, nota2, nota3)

#Se muestra el promedio de cada alumno
print("\n Promedios: ")
for nombre, notas in alumnos.items(): 
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio: 2f}")