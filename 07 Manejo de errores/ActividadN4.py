#Creamos un diccionario vacio para guardar los contactos
agenda = {}

#Cargamos 5 contactos
for i in range(5):
    nombre =input(f"Ingresa el nombre del contacto {i + 1}: ")
    numero = input(f"Ingresa el numero de {nombre}: ")
    agenda[nombre]= numero

#Consultar numero por nombre
consulta = input("¿Que contacto queres consultar?: ")
if consulta in agenda:
    print(f"El numero de {consulta} es {agenda[consulta]}")
else:
    print(f"No se encontro el contacto {consulta} en la agenda.")