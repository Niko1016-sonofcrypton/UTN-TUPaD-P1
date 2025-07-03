#Diccionario actual despues de agregar fruta nueva

precios_frutas = {
    "banana" : 1200,
    "anana" : 2500,
    "melon" :3000,
    "uva" : 1450,
    "naranja" : 1200,
    "manzana" : 1500,
    "pera" :2300,
}

#Actualizacion de precios
precios_frutas["banana"] = 1330
precios_frutas["manzana"] = 1700
precios_frutas["melon"] = 2800

#Creamos la lista con solo nombres de las frutas
frutas = list(precios_frutas.keys())
print(frutas)