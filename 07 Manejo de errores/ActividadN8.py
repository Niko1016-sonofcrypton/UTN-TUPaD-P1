# Se crea diccionario vacío de productos
inventario = {}

# Loop principal
while True:
    producto = input("Ingresá el nombre del producto que querés consultar: ")

    if producto in inventario:
        print(f"Stock actual de '{producto}': {inventario[producto]} unidades")
        agregar = input("¿Querés agregar unidades? (s/n): ").lower()
        if agregar == "s":
            cantidad = int(input("¿Cuántas unidades querés agregar?: "))
            inventario[producto] += cantidad
            print(f"Se agregaron {cantidad} unidades. Nuevo stock: {inventario[producto]}")
    else:
        print(f"El producto '{producto}' no existe en el inventario.")
        agregar_nuevo = input("¿Querés agregarlo? (s/n): ").lower()
        if agregar_nuevo == "s":
            cantidad = int(input("¿Cuántas unidades querés agregar?: "))
            inventario[producto] = cantidad
            print(f"Producto '{producto}' agregado con {cantidad} unidades.")

    print("\n Inventario actual:")
    for nombre, stock in inventario.items():
        print(f" - {nombre}: {stock} unidades")
    print("\n---\n")
