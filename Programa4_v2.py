import random
import numpy as np 

try: 
    with open("dataset.txt", "r") as file:
        dataset = [list(map(int, line.strip().split())) for line in file]
except FileNotFoundError:
    print('el archivo no existe')
    exit()
except Exception as e:
    print("Ocurrió un error:", e)
    exit()

#prueba = [] #el 30% de los datos
# Seleccionar el 30% de los datos de forma aleatoria
num_datos = len(dataset)
num_prueba = int(num_datos * 0.3)
prueba = random.sample(dataset, num_prueba)

# Seleccionar el 70% de los datos restantes
entrenamiento = [fila for fila in dataset if fila not in prueba]

confusion = np.zeros((2,2)) # verdadero positivo, falso positivo, verdadero negativo, falso negativo
vp = confusion[0,0]
fp = confusion[0,1]
vn = confusion[1,0]
fn = confusion[1,1]
R_manhattan = []
R_euclidiana = []


precision = np.zeros((6, 3))



for fila in prueba:
    # Calcular la distancia Manhattan
    distancias_manhattan = []
    for fila_entrenamiento in entrenamiento:
        distancia = sum([abs(fila[i] - fila_entrenamiento[i]) for i in range(1, len(fila) - 1)])
        distancias_manhattan.append((fila_entrenamiento[0], distancia))
    distancias_manhattan.sort()
    # guardar en distancias manhatan indice , valor 
    print(distancias_manhattan[0][1]) 
    
    R_manhattan.append(distancias_manhattan[0][1])
    # Calcular la distancia Euclidiana
    distancias_euclidiana = []
    for fila_entrenamiento in entrenamiento:
        distancia = sum([(fila[i] - fila_entrenamiento[i]) ** 2 for i in range(1, len(fila) - 1)]) ** 0.5
        distancias_euclidiana.append((fila_entrenamiento[0],distancia))
    distancias_euclidiana.sort()
    
    print(distancias_euclidiana[0][1])
    
    R_euclidiana.append(distancias_euclidiana[0][1])
    # Calcular la precisión
    if fila[-1] == R_manhattan[-1]:
        if fila[-1] == 1:
            vp += 1
        else:
            vn += 1
    else:
        if fila[-1] == 1:
            fn += 1
        else:
            fp += 1
    # precision[0][0].append() # verdaderos pos - falsos neg entre los de prueba
    
    