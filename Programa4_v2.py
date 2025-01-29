import random

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

confusion = [[0, 0], [0, 0]] # verdadero positivo, falso positivo, verdadero negativo, falso negativo
vp = confusion[0,0]
fp = confusion[0,1]
vn = confusion[1,0]
fn = confusion[1,1]
R_manhattan = []
R_euclidiana = []


