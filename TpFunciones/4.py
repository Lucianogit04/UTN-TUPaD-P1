import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio
    Args:
        radio (float): Radio del círculo
    Returns:
        float: Área del círculo
    """
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    """
    Calcula el perímetro de un círculo dado su radio
    Args:
        radio (float): Radio del círculo
    Returns:
        float: Perímetro del círculo
    """
    return 2 * math.pi * radio

# Solicitar el radio al usuario
radio = float(input("Ingrese el radio del círculo: "))

# Calcular y mostrar resultados
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"\nPara un círculo de radio {radio}:")
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")
