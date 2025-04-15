def determinar_estacion(hemisferio, mes, dia):
    # Diccionario para mapear los meses a números
    meses = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
        'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
        'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    
    # Convertir el mes a minúsculas y obtener su número
    mes_num = meses[mes.lower()]
    
    # Determinar la estación según el hemisferio
    if hemisferio.upper() == 'N':  # Hemisferio Norte
        if (mes_num == 12 and dia >= 21) or (mes_num == 1) or (mes_num == 2) or (mes_num == 3 and dia <= 20):
            return "Invierno"
        elif (mes_num == 3 and dia >= 21) or (mes_num == 4) or (mes_num == 5) or (mes_num == 6 and dia <= 20):
            return "Primavera"
        elif (mes_num == 6 and dia >= 21) or (mes_num == 7) or (mes_num == 8) or (mes_num == 9 and dia <= 20):
            return "Verano"
        else:
            return "Otoño"
    else:  # Hemisferio Sur
        if (mes_num == 12 and dia >= 21) or (mes_num == 1) or (mes_num == 2) or (mes_num == 3 and dia <= 20):
            return "Verano"
        elif (mes_num == 3 and dia >= 21) or (mes_num == 4) or (mes_num == 5) or (mes_num == 6 and dia <= 20):
            return "Otoño"
        elif (mes_num == 6 and dia >= 21) or (mes_num == 7) or (mes_num == 8) or (mes_num == 9 and dia <= 20):
            return "Invierno"
        else:
            return "Primavera"

def main():
    print("Determinación de la estación del año")
    print("------------------------------------")
    
    # Solicitar información al usuario
    hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ")
    while hemisferio.upper() not in ['N', 'S']:
        print("Por favor, ingresa 'N' para hemisferio norte o 'S' para hemisferio sur.")
        hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ")
    
    mes = input("¿Qué mes es? (ejemplo: enero, febrero, etc.): ")
    while mes.lower() not in ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 
                             'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']:
        print("Por favor, ingresa un mes válido.")
        mes = input("¿Qué mes es? (ejemplo: enero, febrero, etc.): ")
    
    dia = int(input("¿Qué día es? (1-31): "))
    while dia < 1 or dia > 31:
        print("Por favor, ingresa un día válido (1-31).")
        dia = int(input("¿Qué día es? (1-31): "))
    
    # Determinar y mostrar la estación
    estacion = determinar_estacion(hemisferio, mes, dia)
    print(f"\nLa estación actual es: {estacion}")

if __name__ == "__main__":
    main()
