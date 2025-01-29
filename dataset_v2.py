import random
import numpy as np

euclidiana = []
dataset = [  
    [random.randint(0,10) for _ in range(7)] for _ in range(1000)
    ]

matriz_de_prueba = [random.randint(0,10) for _ in range(5)]

matriz_de_entreno = []


#manhattan = [
#    sum(abs(dataset[i][j] - matriz_de_prueba[j]) for j in range(len(matriz_de_prueba))) for i in range(len(dataset))
#]

for fila in dataset: 
    cuadrados = sum((fila[x] - matriz_de_prueba[x]) ** 2 for x in range(len(matriz_de_prueba)))
    euclidiana.append(cuadrados ** 0.5)

print(i for i in dataset)









#print('Kraven: ', kraven)

# for index in range(len(euclidiana)):
#     print('Dist euclidiana en la pelicula no.', index, euclidiana[index])
# print(euclidiana)

# for k in range(len(manhattan)):
#     print('distancia en la pelicula no.', k+1, '',manhattan[k])

# print('pelicula mas cercana a kraven: ', min(euclidiana))

# print('pelicula mas alejada a kraven: ', max(euclidiana))


