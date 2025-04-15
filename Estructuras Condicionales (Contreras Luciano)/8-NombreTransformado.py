nombre = input("Por favor, ingrese su nombre: ")

print("\nSeleccione una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con primera letra mayúscula")

opcion = int(input("\nIngrese el número de la opción deseada (1, 2 o 3): "))

if opcion == 1:
    nombre_transformado = nombre.upper()
elif opcion == 2:
    nombre_transformado = nombre.lower()
elif opcion == 3:
    nombre_transformado = nombre.title()
else:
    print("Opción no válida")
    exit()

print(f"\nResultado: {nombre_transformado}")