#Se solicita la contraseña al usuario
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

#Se verifica la longitud de la contraseña
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")