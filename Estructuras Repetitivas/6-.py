print("Números pares del 100 al 0 (usando for):")
for i in range(100, -1, -2):
    print(i)

print("\nNúmeros pares del 100 al 0 (usando while):")
numero = 100
while numero >= 0:
    print(numero)
    numero -= 2
