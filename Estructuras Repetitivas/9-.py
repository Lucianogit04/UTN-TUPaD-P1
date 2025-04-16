def calcular_media():
    cantidad_numeros = 100  
    suma = 0

    print(f"Ingrese {cantidad_numeros} números enteros:")
    
    for i in range(cantidad_numeros):
        while True:
            try:
                numero = int(input(f"Número {i+1}: "))
                suma += numero
                break
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

    media = suma / cantidad_numeros
    
    print(f"\nLa media de los {cantidad_numeros} números es: {media:.2f}")

if __name__ == "__main__":
    calcular_media()
