def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

# Programa principal
print("Calculadora de Potencias")
print("-----------------------")
base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))
print(f"El resultado es: {potencia(base, exp)}")
