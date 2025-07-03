#Crear la agenda como diccionario vacio
agenda = {}

#Agregar eventos
agenda [("lunes", "09:00")] = "Reunion de equipo"
agenda [("Martes", "14:30")] = "Consulta medica"
agenda [("Miercoles", "11:00")] = "Clase de programacion"
agenda [("Jueves", "18:00")] ="Partido de futbol"
agenda [("Viernes", "10:00")] ="Llamada con cliente"

#Muestra la agenda completa
print("Agenda semanal: ")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")