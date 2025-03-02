import random

with open('C:/Users/Jorge/Desktop/Dr-Ibarra-IA/kmeans/dataset.csv ', "w") as file:
    fila  = ["index"] + ["X" + str(i) for i in range(1, 5)] + ["r"]
    file.write(",".join(fila) + "\n")
    for i in range(1000):
        fila = [i + 1] + [random.randint(1, 7) for _ in range(3)] + [round(random.uniform(0, 2.5), 1)] + [random.randint(1, 3)]
        file.write(",".join(map(str, fila)) + "\n")

print("DATASET GENERADO")


