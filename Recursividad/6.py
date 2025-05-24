def suma_digitos(n):
    # Caso base: si el número es menor a 10, devolvemos el número mismo
    if n < 10:
        return n
    
    # Obtenemos el último dígito usando módulo 10
    ultimo_digito = n % 10
    
    # Obtenemos el número sin el último dígito usando división entera
    numero_sin_ultimo = n // 10
    
    # Sumamos recursivamente el último dígito con la suma de los dígitos restantes
    return ultimo_digito + suma_digitos(numero_sin_ultimo)

if __name__ == "__main__":
    print(suma_digitos(1234))  # Debe imprimir 10
    print(suma_digitos(9))     # Debe imprimir 9
    print(suma_digitos(305))   # Debe imprimir 8
