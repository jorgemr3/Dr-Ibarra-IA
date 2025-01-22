
try: 
    with open("dataset.txt", "r") as file:
        dataset = [list(map(int, line.strip().split())) for line in file]
except FileNotFoundError:
    print('el archivo no existe')
    exit()
except Exception as e:
    print("Ocurrió un error:", e)
    exit()

y = [fila[1:7] for fila in dataset]

# vector problema
vp = [9, 3, 6, 0, 1]

# Distancia Manhattan
R_manhattan = [  
    #sum(abs(dataset[i][j] - kraven[j]) for j in range(len(kraven))) for i in range(len(matriz))
    ]
for fila in y:
    distancia = sum(abs(fila[j] - vp[j]) for j in range(len(vp)))
    R_manhattan.append(distancia)

# Distancia Euclidiana
R_euclidiana = []
for fila in y:
    distancia = sum((fila[j] - vp[j]) ** 2 for j in range(len(vp))) ** 0.5
    R_euclidiana.append(distancia)

#10 más cercanos
matrix = []
for i in range(10):
    min_manhattan = min(R_manhattan)
    pos_manhattan = R_manhattan.index(min_manhattan)
    min_euclidiana = min(R_euclidiana)
    pos_euclidiana = R_euclidiana.index(min_euclidiana)
    matrix.append([pos_manhattan, min_manhattan, pos_euclidiana, min_euclidiana])
    R_manhattan[pos_manhattan] = float("inf")
    R_euclidiana[pos_euclidiana] = float("inf")

print("10 más cercanos (Manhattan || Euclidiana):")
print("Posición (Manhattan), Distancia (Manhattan), Posición (Euclidiana), Distancia (Euclidiana)")
for fila in matrix:
    print(fila)
