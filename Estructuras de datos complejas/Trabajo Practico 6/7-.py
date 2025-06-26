parcial1 = {"Ana", "Luis", "Sofía", "Juan"}
parcial2 = {"Sofía", "Juan", "Marcos", "Lucía"}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)
