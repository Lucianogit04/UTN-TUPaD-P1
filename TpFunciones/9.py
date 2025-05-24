def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.
    
        celsius (float): Temperatura en grados Celsius
        
    Returns:
        float: Temperatura convertida a grados Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Programa principal
def main():
    try:
        # Pedir al usuario la temperatura en Celsius
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        
        # Convertir y mostrar el resultado
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")
        
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()
