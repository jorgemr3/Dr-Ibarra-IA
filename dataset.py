import random

euclidiana = []
matriz = [
    [random.randint(0,10) for _ in range(7)] for _ in range(1000)
    ]

kraven = [random.randint(0,10) for _ in range(5)]

manhattan = [
    sum(abs(matriz[i][j] - kraven[j]) for j in range(len(kraven))) for i in range(len(matriz))
]

for fila in matriz: 
    cuadrados = sum((fila[x] - kraven[x]) ** 2 for x in range(len(kraven)))
    distancia = cuadrados ** 0.5
    euclidiana.append(distancia)

for i in range(len(matriz)): 
    print(matriz[i])

print('Kraven: ', kraven)

# for index in range(len(euclidiana)):
#     print('Dist euclidiana en la pelicula no.', index, euclidiana[index])
# print(euclidiana)

# for k in range(len(manhattan)):
#     print('distancia en la pelicula no.', k+1, '',manhattan[k])

# print('pelicula mas cercana a kraven: ', min(euclidiana))

# print('pelicula mas alejada a kraven: ', max(euclidiana))


