import random

# Generar una matriz de 1000 instancias, cada una con 7 valores, donde la última columna es 0 o 1
with open("dataset.txt", "w") as file:
    for _ in range(1000):
        fila = [random.randint(0, 10) for _ in range(6)] + [random.randint(1, 2)]
        file.write(" ".join(map(str, fila)) + "\n")
