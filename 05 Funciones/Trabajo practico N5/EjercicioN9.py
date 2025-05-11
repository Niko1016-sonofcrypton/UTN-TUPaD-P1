#La lista de compras de diferentes clientes
compras =[["pan", "leche"], ["arroz","fideos","salsa"], ["agua"]]

#Se agrega "jugo" a la lista del tercer cliente 
compras[2].append("jugo")

#Se reemplaza "fideos" por "tallarines" en el segundo cliente
compras[1][1] = "tallarines"

#Se elimina "pan" del primer cliente
compras[0].remove("pan")

#Imprimir la lista resultante por pantalla
print(compras)