def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar del número dado del 1 al 10.
    
    Args:
        numero (int): El número para el cual se generará la tabla de multiplicar
    """
    print(f"\nTabla de multiplicar del {numero}:")
    print("-" * 20)
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Solicitar el número al usuario
try:
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)
except ValueError:
    print("Error: Por favor ingrese un número entero válido.")
