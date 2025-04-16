numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("Error: El número debe ser positivo")
else:
    suma = 0
    for i in range(numero + 1):
        suma += i
    
    print(f"La suma de los números desde 0 hasta {numero} es: {suma}")
