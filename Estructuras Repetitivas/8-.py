def main():
    # Inicializar contadores
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    
    for i in range(100):
        try:
            numero = int(input(f"Ingrese el número {i+1}: "))
            
            # Contar pares e impares
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
                
            if numero > 0:
                positivos += 1
            elif numero < 0:
                negativos += 1
                
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")
            i -= 1  
    
    print("\nResultados:")
    print(f"Cantidad de números pares: {pares}")
    print(f"Cantidad de números impares: {impares}")
    print(f"Cantidad de números positivos: {positivos}")
    print(f"Cantidad de números negativos: {negativos}")

if __name__ == "__main__":
    main()
