def contar_digito(numero, digito):
    # Caso base: si el número es 0, verificamos si el último dígito coincide
    if numero == 0:
        return 1 if digito == 0 else 0
    
    # Caso base: si el número es menor que 10, verificamos si coincide con el dígito
    if numero < 10:
        return 1 if numero == digito else 0
    
    # Caso recursivo: verificamos el último dígito y llamamos recursivamente con el resto del número
    ultimo_digito = numero % 10
    resto_numero = numero // 10
    
    # Si el último dígito coincide, sumamos 1 al resultado de la llamada recursiva
    if ultimo_digito == digito:
        return 1 + contar_digito(resto_numero, digito)
    else:
        return contar_digito(resto_numero, digito)

if __name__ == "__main__":
    print(contar_digito(12345, 1))  # Debería imprimir 1
    print(contar_digito(11111, 1))  # Debería imprimir 5
    print(contar_digito(12345, 0))  # Debería imprimir 0
    print(contar_digito(1000, 0))   # Debería imprimir 3
