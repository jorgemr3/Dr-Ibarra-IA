import random

with open("dataset.txt", "w") as file:
    for i in range(1000):
        fila = [i +1] + [random.randint(0, 10) for _ in range(6)] + [random.randint(1, 2)]
        file.write(" ".join(map(str, fila)) + "\n")
