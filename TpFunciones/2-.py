def saludar_usuario(nombre):
    """
    Función que recibe un nombre y devuelve un saludo personalizado.
    
    Args:
        nombre (str): El nombre de la persona a saludar
        
    Returns:
        str: Un saludo personalizado
    """
    return f"¡Hola {nombre}!"

if __name__ == "__main__":
    nombre_usuario = input("Por favor, ingrese su nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)
