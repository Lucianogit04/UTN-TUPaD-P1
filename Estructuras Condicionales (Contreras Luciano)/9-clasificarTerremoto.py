def clasificar_terremoto(magnitud):
    if magnitud < 3:
        return "Muy leve (imperceptible)"
    elif 3 <= magnitud < 4:
        return "Leve (ligeramente perceptible)"
    elif 4 <= magnitud < 5:
        return "Moderado (sentido por personas, pero generalmente no causa daños)"
    elif 5 <= magnitud < 6:
        return "Fuerte (puede causar daños en estructuras débiles)"
    elif 6 <= magnitud < 7:
        return "Muy Fuerte (puede causar daños significativos)"
    else:
        return "Extremo (puede causar graves daños a gran escala)"

def main():
    try:
        magnitud = float(input("Ingrese la magnitud del terremoto: "))
        if magnitud < 0:
            print("Error: La magnitud no puede ser negativa")
            return
        resultado = clasificar_terremoto(magnitud)
        print(f"La clasificación del terremoto es: {resultado}")
    except ValueError:
        print("Error: Por favor ingrese un número válido")

if __name__ == "__main__":
    main()
