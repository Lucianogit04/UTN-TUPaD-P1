texto = input("Por favor, ingrese una frase o palabra: ")

if texto[-1].lower() in ['a', 'e', 'i', 'o', 'u']:
    texto += '!'

print(texto)