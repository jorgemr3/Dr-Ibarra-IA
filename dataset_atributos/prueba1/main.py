import numpy as np
import random
import pandas as pd
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# import matplotlib.pyplot as plt

def entropia(conjunto):
    conteo_clases = conjunto.iloc[:, -1].value_counts()
    numeros_si = conteo_clases.get('si', 0)  # Si no hay 'si', devuelve 0
    numeros_no = conteo_clases.get('no', 0)  # Si no hay 'no', devuelve 0
    totales = numeros_si + numeros_no
    p_si = numeros_si / totales
    p_no = numeros_no / totales
    return -p_si * np.log2(p_si) - p_no * np.log2(p_no)

# def entropia_atributo(atributo, entrenamiento):
#     entropia = 0
#     for valor in entrenamiento[atributo].unique():
#         subconjunto = entrenamiento[entrenamiento[atributo] == valor]
#         entropia_subconjunto = entropia(subconjunto)
#         entropia += len(subconjunto) / len(entrenamiento) * entropia_subconjunto
#     return entropia

# def ganancia():
    # retornar con formula de ganancia 
    # ganancia = sumatoria de (#casos si/no del atributo n / numero total de casos de los atributos) * entropia(atributo n)
    # return ganancia



df = pd.read_csv("C:/Users/Jorge/Desktop/Dr-Ibarra-IA/dataset_atributos/prueba1/dataset_v2.csv")

temp = int(len(df) * 0.3)  # 30% de los datos
indices = list(range(len(df)))
random.shuffle(indices)
entrenamiento = df.iloc[indices[temp:]]  # 70% de los datos
prueba = df.iloc[indices[:temp]]  # 30% de los datos

Earbol = entropia(entrenamiento)






