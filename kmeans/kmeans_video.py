import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#  TODO: Cambiar el valor de K
K = 4


def mostrar_clusters():
    # Visualización de los clusters
    plt.scatter(df_copia['X2'], df_copia['X3'], c=df_copia['cluster'], cmap='rainbow')
    plt.xlabel('X2')
    plt.ylabel('X3')
    plt.title('Clustering con K-Means')
    # plt.grid()
    plt.show()

def mostrar_centroides():
    plt.scatter(df_copia['X2'], df_copia['X3'], c=df_copia['cluster'], cmap='rainbow')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='black', marker='x', s=85)
    # extrae las coordenadas en X (kmeans.cluster_centers_[:, 0]) 
    # y Y (kmeans.cluster_centers_[:, 1]) 
    # de los centroides
    plt.xlabel('X2')
    plt.ylabel('X3')
    plt.title('Centroides por cluster de datos')
    plt.show()

def elbow():
    # metodo del codo
    codo = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, n_init='auto', random_state=42)
        kmeans.fit(x)
        codo.append(kmeans.inertia_)
    plt.plot(range(1, 11), codo, marker='x')
    plt.xlabel('Número de clusters')
    plt.title('Método del codo, mientras menos inertia mejor')
    plt.grid()
    plt.ylabel('Inertia')
    plt.show()
    # Visualización inicial
    plt.scatter(df['X2'], df['X3'])
    plt.xlabel('X2')
    plt.ylabel('X3')
    plt.title('Distribución de los puntos')
    plt.show()



# Cargar el dataset
df = pd.read_csv('C:/Users/Jorge/Desktop/Dr-Ibarra-IA/kmeans/dataset.csv')
# Selección de características (x2 y x3)
x = df.iloc[:, 2:4]

# metodo del codo
elbow()


# Aplicar KMeans con K clusters
kmeans = KMeans(n_clusters=K, n_init='auto', random_state=42)
df_clusterizado = kmeans.fit_predict(x)

# Crear una copia del DataFrame con los clusters
df_copia = df.copy()
df_copia['cluster'] = df_clusterizado

print('-------dataset con grupos---------')
print(df_copia.head())

mostrar_clusters()

print('-'*50)
# Mostrar los centroides
print('Coordenadas de centroides')
print('')
for i in kmeans.cluster_centers_:
    print(i)
# print('-'*50)

mostrar_centroides()





