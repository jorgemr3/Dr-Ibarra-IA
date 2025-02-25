try: 
    with open("C:/Users/Jorge/Desktop/Dr-Ibarra-IA/dataset_Sab_1feb/dataset.txt", "r") as file:
        dataset = [list(map(int, line.strip().split())) for line in file]
except FileNotFoundError:
    print('el archivo no existe')
    exit()
except Exception as e:
    print("Ocurrió un error:", e)
    exit()
    
import random
import numpy as np 
from collections import Counter

    
    
#region CONFIGURACION
num_prueba = int(len(dataset) * 0.3) # 30% de los datos 

indices = list(range(len(dataset)))
# print(indices)
random.shuffle(indices)
# mix(indices)
# print(indices)
entrenamiento = [dataset[i] for i in indices[:num_prueba]] #300, 200, 100
prueba = [dataset[i] for i in indices[num_prueba:]] # 700, 800,900

K = 140  # Número de óptimos a considerar 

#endregion

metricas = ['manhattan', 'euclidiana', 'euclidiana_normalizada', 'coseno', 'Sorensen_Dice', 'Jaccard']

# arreglo de ceros de tamanio 2 x 2 por metricas 
confusion_metrics = {metrica: np.zeros((2, 2), dtype=int) for metrica in metricas}

def actualizar_confusion(prediccion, real, matriz):
    """Actualiza la matriz de confusión, si real es 1 y la prediccion es 1 es verdadero positivo, si prediccion no es 1 entonces es falso negativo"""
    if real == 1:
        if prediccion == 1: matriz[0, 0] += 1  # VP real 1 prediccion 1
        else: matriz[1, 0] += 1               # VN real 1 prediccion 2
    else: # real == 2
        if prediccion == 1: matriz[0, 1] += 1  # FP real 2 prediccion 1
        else: matriz[1, 1] += 1               # FN real 2 prediccion 2

for fila in entrenamiento:
    resultados = {
        'manhattan': [],
        'euclidiana': [],
        'euclidiana_normalizada': [],
        'coseno': [],
        'Sorensen_Dice': [],
        'Jaccard': []
    }
    # la informacion de los resultados se guarda en un diccionario de arreglos 
    #------------------------------------------
    # fila[i] = x 
    # fila_entrenamiento[i] = y
    #------------------------------------------
    #region CALC. METRICAS
    x_cuadrada = sum(fila[i]**2 for i in range(1, len(fila)-1)) # ciclo de x al cuadrado
    # ciclo_multiplicativo = sum(fila[i] * fila_entrenamiento[i] for i in range(1, len(fila)-1)) # ciclo de x por y en la posicion i
    # y_cuadrada = sum(fila_entrenamiento[i]**2 for i in range(1, len(fila)-1)) # ciclo de y al cuadrado
     
    #   Calcular la distancia Manhattan
    for row in prueba:
        distancia  = sum([abs(fila[i] - row[i]) for i in range(1, len(fila) - 1)])
        resultados['manhattan'].append((row[0], distancia, row[-1])) # agregar la columna de respuesta (indice, valor, respuesta)
    resultados['manhattan'].sort()
   
      # Calcular la distancia euclidiana normal
    for row in prueba:
        distancia = sum((fila[i] - row[i]) **2 for i in range(1, len(fila)-1)) ** 0.5
        resultados['euclidiana'].append((row[0],distancia, row[-1]))
    resultados['euclidiana'].sort()
    
     # Calcular la distancia eucidiana normalizada
    for row in prueba:
        distancia = sum(fila[i]**2 - 2*(fila[i] * row[i]) + row[i]**2 for i in range(1, len(fila)-1))
        # distancia = sum(fila[i] - fila_entrenamiento[i])**2 for i in range(1, len(fila)-1)
        resultados['euclidiana_normalizada'].append((row[0], distancia, row[-1]))
    resultados['euclidiana_normalizada'].sort()
    
    # Calcular la distancia coseno
    for row in prueba:
        similitud = sum(fila[i] * row[i] for i in range(1, len(fila)-1)) / (x_cuadrada * sum(row[i]**2 for i in range(1, len(fila)-1)))**0.5
        resultados['coseno'].append((row[0], similitud, row[-1]))
    resultados['coseno'].sort(reverse=True) 
    
    # Calcular la distancia Sorensen-Dice
    for row in prueba:
        distancia = (2 * sum(fila[i] * row[i] for i in range(1, len(fila)-1))) / (x_cuadrada + sum(row[i]**2 for i in range(1, len(fila)-1)))
        resultados['Sorensen_Dice'].append((row[0], distancia, row[-1]))
    resultados['Sorensen_Dice'].sort(reverse=True)
    
    # calcular la distancia Jaccard
    for row in prueba:
        suma_xy = sum(fila[i] * row[i] for i in range(1, len(fila)-1))
        suma_x2 = x_cuadrada
        suma_y2 = sum(row[i]**2 for i in range(1, len(fila)-1))
        distancia = suma_xy / (suma_x2 + suma_y2 - suma_xy) if (suma_x2 + suma_y2 - suma_xy) != 0 else 0
        # distancia =  sum(fila[i] * fila_entrenamiento[i] for i in range(1, len(fila)-1)) / x_cuadrada + sum(fila_entrenamiento[i]**2 for i in range(1, len(fila)-1)) - sum(fila[i] * fila_entrenamiento[i] for i in range(1, len(fila)-1))
        resultados['Jaccard'].append((row[0], distancia, row[-1]))
    resultados['Jaccard'].sort(reverse=True)
    #endregion
    #region fill confusion matrix
    for metrica in metricas:
        # Ordenar y tomar los K optimos
        # resultados[metrica].sort(key=lambda x: x[1])
        vecinos = resultados[metrica][:K]
        
        # Obtener clase mayoritaria
        clases = [clase for (_, _, clase) in vecinos]
        conteo = Counter(clases)
        prediccion = conteo.most_common(1)[0][0]
        
        # Desempate por distancia más cercana
        if len(conteo) > 1 and conteo.most_common()[0][1] == conteo.most_common()[1][1]:
            prediccion = vecinos[0][2]  # Clase del vecino más cercano
        
        
        
        #TODO: error detectado, la matriz de confusion siempre marca 0, 300 porque la prediccion y el real son lo mismo 
        #TODO: arreglar las dos lineas anteriores
        #TODO: 
        # Actualizar matriz de confusión
        # actualizar_confusion(fila[-1], vecinos[-1], confusion_metrics[metrica])
        actualizar_confusion(prediccion, fila[-1], confusion_metrics[metrica])
    #endregion

#region PRECISION
# Función para calcular precisión
def ibarra_precision(matriz):
    vp = matriz[0, 0] # verdadero positivo 
    fn = matriz[1, 0] # falso negativo 
    #falso positivo y verdadero negativo
    # se descartan porque no son necesarios para calcular la precisión
    temp = vp + fn  
    return float(temp / len(entrenamiento))

def precision(matriz):
    vp = matriz[0, 0]
    fp = matriz[0, 1]
    temp = vp + fp
    return vp / temp  if temp != 0 else 0

def recall(matriz):
    vp = matriz[0, 0]
    fn = matriz[1, 0]
    temp = vp + fn
    return vp / temp if temp != 0 else 0

def accuracy(matriz):
    vp = matriz[0, 0]
    vn = matriz[1, 1]
    total = matriz.sum()
    return (vp + vn) / total if total != 0 else 0

#endregion

for i in confusion_metrics:  print(confusion_metrics[i])
# print(prediccion)
# region Resultados 
print(f" ======== Precisión con K={K} ======== ")
for metrica in metricas:
    print(f"{metrica.upper():<20}: Precision: {precision(confusion_metrics[metrica]):.3%}, Sensibilidad: {recall(confusion_metrics[metrica]):.3%}, Exactitud: {accuracy(confusion_metrics[metrica]):.3%}")
print('')
print('============ Precision con la formula del Dr Ibarra (Pizarron) ============' )
for metrica in metricas:
    print(f"{metrica.upper():<20}: Precision: {ibarra_precision(confusion_metrics[metrica]):.3%})")
#endregion