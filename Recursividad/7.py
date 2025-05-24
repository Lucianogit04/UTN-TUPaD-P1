def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Ejemplos de uso
if __name__ == "__main__":
    # Prueba con diferentes valores
    print(contar_bloques(3))  # Debería dar 6 (3 + 2 + 1)
    print(contar_bloques(4))  # Debería dar 10 (4 + 3 + 2 + 1)
    print(contar_bloques(5))  # Debería dar 15 (5 + 4 + 3 + 2 + 1)
