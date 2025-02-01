import random
import numpy as np 
from collections import Counter

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
indices = list(range(num_datos))
random.shuffle(indices)
prueba = [dataset[i] for i in indices[:num_prueba]]
entrenamiento = [dataset[i] for i in indices[num_prueba:]]

# Configuración
K = 140  # Número de óptimos a considerar
'''
Cuando se trabaja con una diferente proporcion, porfavor modificar variable K

con proporcion 70% - 30% se recomienda K = 140

con proporcion 80% - 20% se recomienda K = 160

con proporcion 90% - 10% se recomienda K = 180 

siempre respetando el 20% de las distancias o metricas (asi lo dice ibarra lol)

'''
metricas = ['manhattan', 'euclidiana', 'euclidiana_normalizada', 'coseno', 'Sorensen_Dice', 'Jaccard']

# Inicializar matriz de confusión para cada métrica
confusion_metrics = {metrica: np.zeros((2, 2), dtype=int) for metrica in metricas}

def actualizar_confusion(prediccion, real, matriz):
    """Actualiza la matriz de confusión"""
    if real == 1:
        if prediccion == 1: matriz[0, 0] += 1  # VP
        else: matriz[1, 0] += 1               # FN
    else:
        if prediccion == 1: matriz[0, 1] += 1  # FP
        else: matriz[1, 1] += 1               # VN


for fila in prueba:
    resultados = {
        'manhattan': [],
        'euclidiana': [],
        'euclidiana_normalizada': [],
        'coseno': [],
        'Sorensen_Dice': [],
        'Jaccard': []
    }
    
    #------------------------------------------
    # fila[i] = x 
    # fila_entrenamiento[i] = y
    #------------------------------------------
    
    x_cuadrada = sum(fila[i]**2 for i in range(1, len(fila)-1)) # ciclo de x al cuadrado
    # ciclo_multiplicativo = sum(fila[i] * fila_entrenamiento[i] for i in range(1, len(fila)-1)) # ciclo de x por y en la posicion i
    # y_cuadrada = sum(fila_entrenamiento[i]**2 for i in range(1, len(fila)-1)) # ciclo de y al cuadrado
     
    #   Calcular la distancia Manhattan
    for fila_entrenamiento in entrenamiento:
        distancia = sum([abs(fila[i] - fila_entrenamiento[i]) for i in range(1, len(fila) - 1)])
        resultados['manhattan'].append((fila_entrenamiento[0], distancia, fila_entrenamiento[-1])) # agregar la columna de respuesta (indice, valor, respuesta)
    resultados['manhattan'].sort()
   
      # Calcular la distancia euclidiana normal
    for fila_entrenamiento in entrenamiento:
        distancia = sum((fila[i] - fila_entrenamiento[i]) **2 for i in range(1, len(fila)-1)) ** 0.5
        resultados['euclidiana'].append((fila_entrenamiento[0],distancia, fila_entrenamiento[-1]))
    resultados['euclidiana'].sort()
    
     # Calcular la distancia eucidiana normalizada
    for fila_entrenamiento in entrenamiento:
        distancia = sum(fila[i]**2 - 2*(fila[i] * fila_entrenamiento[i]) + fila_entrenamiento[i]**2 for i in range(1, len(fila)-1))
        # distancia = sum(fila[i] - fila_entrenamiento[i])**2 for i in range(1, len(fila)-1)
        resultados['euclidiana_normalizada'].append((fila_entrenamiento[0], distancia, fila_entrenamiento[-1]))
    resultados['euclidiana_normalizada'].sort()
    
    # Calcular la distancia coseno
    for fila_entrenamiento in entrenamiento:
        similitud = sum(fila[i] * fila_entrenamiento[i] for i in range(1, len(fila)-1)) / (x_cuadrada * sum(fila_entrenamiento[i]**2 for i in range(1, len(fila)-1)))**0.5
        resultados['coseno'].append((fila_entrenamiento[0], similitud, fila_entrenamiento[-1]))
    resultados['coseno'].sort()
    
    # Calcular la distancia Sorensen-Dice
    for fila_entrenamiento in entrenamiento:
        distancia = (2 * sum(fila[i] * fila_entrenamiento[i] for i in range(1, len(fila)-1))) / (x_cuadrada + sum(fila_entrenamiento[i]**2 for i in range(1, len(fila)-1)))
        resultados['Sorensen_Dice'].append((fila_entrenamiento[0], distancia, fila_entrenamiento[-1]))
    resultados['Sorensen_Dice'].sort()
    
    # calcular la distancia Jaccard
    for fila_entrenamiento in entrenamiento:
        distancia =  sum(fila[i] * fila_entrenamiento[i] for i in range(1, len(fila)-1)) / x_cuadrada + sum(fila_entrenamiento[i]**2 for i in range(1, len(fila)-1)) - sum(fila[i] * fila_entrenamiento[i] for i in range(1, len(fila)-1))
        resultados['Jaccard'].append((fila_entrenamiento[0], distancia, fila_entrenamiento[-1]))
    resultados['Jaccard'].sort()
    
    for metrica in metricas:
        # Ordenar y tomar los K vecinos
        resultados[metrica].sort(key=lambda x: x[0])
        vecinos = resultados[metrica][:K]
        
        # Obtener clase mayoritaria
        clases = [clase for (_, _, clase) in vecinos]
        conteo = Counter(clases)
        prediccion = conteo.most_common(1)[0][0]
        
        # Desempate por distancia más cercana
        if len(conteo) > 1 and conteo.most_common()[0][1] == conteo.most_common()[1][1]:
            prediccion = vecinos[0][1]  # Clase del vecino más cercano
        
        # Actualizar matriz de confusión
        actualizar_confusion(prediccion, fila_entrenamiento[-1], confusion_metrics[metrica])
    
# Función para calcular precisión
def precision(matriz):
    vp = matriz[0, 0] # verdadero positivo 
    fn = matriz[1, 0] # falso negativo 
    temp = vp + fn  
    return float(temp / len(prueba))

# Resultados finales
print(f" === Precisión con K={K} === ")
for metrica in metricas:
    print(f"{metrica.upper():<20}: {precision(confusion_metrics[metrica]):.3%}")


''' descomentar para ver los resultados de las distancias '''
# for i in manhattan:  print(i)  

# for i in euclidiana:  print(i) 

# for i in euclidiana_normalizada:  print(i)

# for i in coseno:  print(i)

# for i in Sorensen_Dice:  print(i)

# for i in Jaccard:  print(i)

     
    # guardar en distancias manhatan indice , valor
    
    
    
    # print(distancias_euclidiana[0][1])
    
     # guardar en distancias manhatan indice , valor 
    # print(distancias_manhattan[0][1]) 
    # R_manhattan.append(distancias_manhattan[0][1])
    # Calcular la distancia Euclidiana
    
    
    # R_euclidiana.append(distancias_euclidiana[0][1])
    # Calcular la precisión
    # si la respuesta en el pronostico (entrenamiento) es igual a la respuesta en lo predecido es 1 en vp 
    # si la respuesta en pronostico es diferente a la respuesta en lo predecido es 1 en fp
    # si la respuesta en predecido es diferente a la respuesta en el pronostico es 1 en vn
    # si la respuesta en predecido es igual a la respuesta en el pronostico es 1 en fn
    # 
    # if fila[-1] == R_manhattan[-1]:
    #     if fila[-1] == 1:
    #         vp += 1
    #     else:
    #         vn += 1
    # else:
    #     if fila[-1] == 1:
    #         fn += 1
    #     else:
    #         fp += 1
    # Seleccionar el 70% de los datos restantes
# entrenamiento = [fila for fila in dataset if fila not in prueba]


# confusion = np.zeros((2, 2), dtype=int)# verdadero positivo, falso positivo, verdadero negativo, falso negativo
# vp = confusion[0,0]
# fp = confusion[0,1]
# vn = confusion[1,0]
# fn = confusion[1,1]
# R_manhattan = [] # agregar la columna de 
# R_euclidiana = []
    
    