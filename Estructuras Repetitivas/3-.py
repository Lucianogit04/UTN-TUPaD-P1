valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

inicio = min(valor1, valor2)
fin = max(valor1, valor2)

suma = 0

for numero in range(inicio + 1, fin):
    suma += numero

print(f"La suma de los números entre {inicio} y {fin} (excluyendo los límites) es: {suma}")
