frase = input("Ingresá una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("Cantidad de veces que aparece cada palabra:")
print(contador_palabras)
