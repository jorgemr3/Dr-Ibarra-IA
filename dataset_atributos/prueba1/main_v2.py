import numpy as np
import pandas as pd
import random

def entropia(conjunto):

    conteo_clases = conjunto.iloc[:, -1].value_counts()
    numeros_si = conteo_clases.get('si', 0)
    numeros_no = conteo_clases.get('no', 0)
    totales = numeros_si + numeros_no
    
    p_si = numeros_si / totales
    p_no = numeros_no / totales
    
    entropia_val = 0.0
    if p_si > 0:
        entropia_val += -p_si * np.log2(p_si)
    if p_no > 0:
        entropia_val += -p_no * np.log2(p_no)
    
    return entropia_val if not np.isnan(entropia_val) else 0.0

def calcular_ganancia(variable, entrenamiento, Earbol):
    # Crear tabla de frecuencias
    tabla = entrenamiento.groupby([variable, entrenamiento.iloc[:, -1]]).size().unstack(fill_value=0)
    tabla = tabla.reindex(columns=['si', 'no'], fill_value=0)
    
    # Calcular totales y entropías
    tabla['casos'] = tabla.sum(axis=1)
    tabla['E'] = 0.0
    
    for valor in tabla.index:
        subconjunto = entrenamiento[entrenamiento[variable] == valor]
        tabla.loc[valor, 'E'] = entropia(subconjunto)
    
    # Calcular entropía ponderada
    tabla['peso'] = tabla['casos'] / len(entrenamiento)
    entropia_variable = (tabla['peso'] * tabla['E']).sum()
    
    # Formatear tabla de salida
    tabla_print = tabla[['si', 'no', 'casos', 'E']].reset_index()
    tabla_print.columns = ['Atributo', 'si', 'no', 'casos', 'E']
    return Earbol - entropia_variable , tabla_print

def dividir(conjunto):
    indices = conjunto.index.tolist()
    random.shuffle(indices) # mezclar indices 
    tam_prueba = int(len(conjunto) * 0.3)
    entrenamiento = conjunto.iloc[indices[tam_prueba:]] # 70%
    prueba = conjunto.iloc[indices[:tam_prueba]] # 30%
    return entrenamiento, prueba

def main():
    df = pd.read_csv("C:/Users/Jorge/Desktop/Dr-Ibarra-IA/dataset_atributos/prueba1/dataset_v2.csv") #leer csv
    
    entrenamiento, prueba = dividir(df)
    # print(entrenamiento)
    # print(prueba)
    Earbol = entropia(entrenamiento)
    # prueba = prueba.reset_index(drop=True)
    # prueba = prueba.drop(columns=['si/no'])
    # prueba = prueba.drop(columns=['index'])
    
    ganancias= []    
    
    variables = entrenamiento.columns[1:-1] # se salta la columna de respuesta (si/no) Saltarse la primera columna INDEX jaja
    
    for var in variables: 
        print(f"\nVariable: {var}")
        ganancia, tabla = calcular_ganancia(var, entrenamiento, Earbol)
        
        ganancias.append(float(ganancia))
        
        # Imprimir tabla
        print(tabla.to_string(index=False))
        print(f"Ganancia para {var}: {ganancia:.4f}\n")
        print("-"*50)
    
    print(f'Nodo mas alto del arbol: {max(ganancias)}')
    
if __name__ == "__main__":
    main()

    # ya saque la ganancia por variable, ahora generar el arbol de decision
    # es manual jaja