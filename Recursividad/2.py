def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Ingrese hasta qué posición quiere ver la serie de Fibonacci: "))

print("\nSerie de Fibonacci:")
for i in range(n + 1):
    print(f"Posición {i}: {fibonacci(i)}")
