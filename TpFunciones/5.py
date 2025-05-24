def segundos_a_horas(segundos):
    """
    Convierte segundos a horas.
    
    Args:
        segundos (float): Cantidad de segundos a convertir
        
    Returns:
        float: Cantidad de horas correspondiente
    """
    return segundos / 3600  # 1 hora = 3600 segundos

# Solicitar los segundos al usuario
try:
    segundos = float(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")
except ValueError:
    print("Error: Por favor ingrese un número válido")
