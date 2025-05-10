#Se solicita la edad a la persona
edad = int(input("Ingrese su edad: "))

#Se clasifica la edad del usuario y segun la edad aparece la categoria
if edad < 12:
    print("Categoria: Niño/a")
elif edad >= 12 and edad < 18:
    print("Categoria: Adolecente")
elif edad >= 18 and edad < 30:
    print("Categoria: Adulto/a joven")
else:
    print("Categoria: Adulto/a")