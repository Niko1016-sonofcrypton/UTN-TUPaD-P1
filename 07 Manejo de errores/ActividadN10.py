#Diccionario: paises como claves y capitales como valores

paises_a_capitales ={
    "Argentina": "Buenos Aires",
    "brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asuncion"
}

#Se crea un nuevo diccionarop con capitales como claves y paises como valores
capitales_a_paises = {}

for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais

#Se muestra el resultado
print("Diccionario invertido (Capitales -> paises): ")
for capital, pais in capitales_a_paises.items():
    print(f"{capital}: {pais}")