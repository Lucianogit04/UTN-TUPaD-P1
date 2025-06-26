
stock_productos = {}

while True:
    producto = input("Ingresá el nombre del producto (o 'salir' para terminar): ")
    if producto.lower() == "salir":
        break

    if producto in stock_productos:
        print(f"Stock actual de {producto}: {stock_productos[producto]}")
        agregar = input("¿Querés agregar unidades? (s/n): ")
        if agregar.lower() == "s":
            unidades = int(input("¿Cuántas unidades querés agregar?: "))
            stock_productos[producto] += unidades
            print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
    else:
        print(f"{producto} no existe en el stock.")
        agregar = input("¿Querés agregarlo como nuevo producto? (s/n): ")
        if agregar.lower() == "s":
            unidades = int(input("¿Cuántas unidades tiene?: "))
            stock_productos[producto] = unidades
            print(f"{producto} agregado con {unidades} unidades.")

print("\nStock final de productos:")
for prod, stock in stock_productos.items():
    print(f"{prod}: {stock}")
