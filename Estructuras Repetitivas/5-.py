import random

def juego_adivinanza():
    numero_secreto = random.randint(0, 9)
    intentos = 0
    
    print("¡Bienvenido al juego de adivinanza!")
    print("Tienes que adivinar un número entre 0 y 9.")
    
    while True:
        try:
            intento = int(input("Ingresa tu número: "))
            intentos += 1
            
            if intento < 0 or intento > 9:
                print("Por favor, ingresa un número entre 0 y 9.")
                continue
                
            if intento == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
            elif intento < numero_secreto:
                print("El número es mayor. ¡Intenta de nuevo!")
            else:
                print("El número es menor. ¡Intenta de nuevo!")
                
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    juego_adivinanza()
