import random

with open("C:/Users/Jorge/Desktop/Dr-Ibarra-IA/dataset_Sab_1feb/dataset.txt", "w") as file:
    for i in range(1000):
        fila = [i + 1] + [random.randint(1, 10) for _ in range(6)] + [random.randint(1, 2)]
        file.write(" ".join(map(str, fila)) + "\n")

print("DATASET GENERADO")

# dataset de mil instancias de 6 atributos y una clase
# ejemplo de formato de instancia i
'''
1 8 5 7 3 9 6 2
2 1 6 10 3 3 1 1
3 1 7 8 0 2 2 2

'''
# el formato usado es el siguiente:

# un numero entero que identifica la instancia
# seguido de 6 numeros enteros que representan los atributos de la instancia
# y un numero entero que representa la clase de la instancia

#dando como resultado algo parecido a: 

# index atributo1 atributo2 atributo3 atributo4 atributo5 atributo6 clase

# separado por espacios y saltos de linea al final de cada instancia
# tamanio aproximado del dataset 1000 * 7
# por cada instancia se genera numeros aleatorios entre 0 y 10 para los atributos y 1 y 2 para la clase
# los numeros del 1 al 10 son repetibles entre si pero la clase es unica para cada instancia
