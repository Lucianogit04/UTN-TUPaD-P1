agenda = {
    ("lunes", "09:00"): "Reunión de equipo",
    ("martes", "14:30"): "Clase de Bases de Datos",
    ("miércoles", "11:00"): "Llamada con proveedor",
    ("jueves", "16:00"): "Entrenamiento técnico",
    ("viernes", "10:00"): "Presentación de proyecto"
}

dia = input("Ingresá un día (en minúsculas): ")
hora = input("Ingresá la hora (formato HH:MM): ")

clave = (dia, hora)
evento = agenda.get(clave)

if evento:
    print(f"A las {hora} del {dia} tenés: {evento}")
else:
    print("No hay eventos agendados para ese día y hora.")