def decimal_a_binario(n):
    # Caso base: si el número es 0 o 1, retornamos su representación en string
    if n <= 1:
        return str(n)
    # Caso recursivo: dividimos el número por 2 y concatenamos el residuo
    return decimal_a_binario(n // 2) + str(n % 2)

# Ejemplos de uso
if __name__ == "__main__":
    # Pruebas con diferentes números
    numeros_prueba = [5, 10, 15, 20, 42]
    
    for num in numeros_prueba:
        resultado = decimal_a_binario(num)
        print(f"El número {num} en binario es: {resultado}")
