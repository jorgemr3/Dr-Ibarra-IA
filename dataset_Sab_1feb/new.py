import pandas as pd
import matplotlib.pyplot as plt

# Datos de ejemplo
data = {
    'K': [140, 160, 180],
    'Promedio': [49.33, 50.5, 51.0],
    'Mediana': [50.33, 50.5, 51.0],
    'Desviación Estándar': [3.02, 2.85, 2.10]
}

df = pd.DataFrame(data)

# Gráfico de barras
df.plot(x='K', y=['Promedio', 'Mediana'], kind='bar', title='Comparación de Métricas')
plt.ylabel('Precisión (%)')
plt.show()