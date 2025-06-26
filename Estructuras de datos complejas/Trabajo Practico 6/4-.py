agenda = {}

for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero

consulta = input("¿De qué contacto querés saber el número? ")
if consulta in agenda:
    print(f"El número de {consulta} es: {agenda[consulta]}")
else:
    print("Ese contacto no está en la agenda.")