def calcular_promedio(a, b, c):
    """
    Calcula el promedio de tres números.
    
        a (float): Primer número
        b (float): Segundo número
        c (float): Tercer número
    
    Returns:
        float: El promedio de los tres números
    """
    return (a + b + c) / 3

# Solicitar los números al usuario
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    
    # Calcular y mostrar el promedio
    resultado = calcular_promedio(num1, num2, num3)
    print(f"\nEl promedio de {num1}, {num2} y {num3} es: {resultado:.2f}")
except ValueError:
    print("Error: Por favor ingrese números válidos.")
