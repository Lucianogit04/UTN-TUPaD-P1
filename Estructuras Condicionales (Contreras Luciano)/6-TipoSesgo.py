import random
from statistics import mode, median, mean


numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)


if media > mediana > moda:
    print("La distribución tiene sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo o a la izquierda")
else:
    print("La distribución no tiene sesgo")


print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda}")