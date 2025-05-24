def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC)
    
    Args:
        peso (float): Peso en kilogramos
        altura (float): Altura en metros
    
    Returns:
        float: Índice de Masa Corporal
    """
    return peso / (altura ** 2)

# Programa principal
def main():
    try:
        # Solicitar datos al usuario
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))
        
        # Validar que los valores sean positivos
        if peso <= 0 or altura <= 0:
            print("Error: El peso y la altura deben ser valores positivos.")
            return
        
        # Calcular IMC
        imc = calcular_imc(peso, altura)
        
        # Mostrar resultado con dos decimales
        print(f"\nSu Índice de Masa Corporal (IMC) es: {imc:.2f}")
        
        # Mostrar categoría según IMC
        if imc < 18.5:
            categoria = "Bajo peso"
        elif imc < 25:
            categoria = "Peso normal"
        elif imc < 30:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidad"
            
        print(f"Categoría: {categoria}")
        
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
