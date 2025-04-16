total = 0

print("Ingrese números enteros para sumar (ingrese 0 para terminar):")

while True:
    try:
        numero = int(input("Ingrese un número: "))
        if numero == 0:
            break
        total += numero
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

print(f"La suma total de los números ingresados es: {total}")
