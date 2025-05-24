def operaciones_basicas(a, b):
    """
    Realiza las operaciones básicas (suma, resta, multiplicación y división) con dos números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
        
    Returns:
        tuple: Tupla con los resultados de (suma, resta, multiplicación, división)
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    # Manejo de división por cero
    try:
        division = a / b
    except ZeroDivisionError:
        division = "No es posible dividir por cero"
    
    return (suma, resta, multiplicacion, division)

# Ejemplo de uso
if __name__ == "__main__":
    # Prueba con números positivos
    num1 = 10
    num2 = 5
    resultados = operaciones_basicas(num1, num2)
    
    print(f"Números utilizados: {num1} y {num2}")
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")
    
    # Prueba con división por cero
    print("\nPrueba con división por cero:")
    resultados_cero = operaciones_basicas(10, 0)
    print(f"Resultados con b=0: {resultados_cero}")
