import random
import numpy
# from matplotlib import pyplot 
def maximMinim(dsT):
    maxim = []
    minim = []
    for i in dsT:
        maxim.append(max(i))
        minim.append(min(i))
    return maxim, minim

def ActualizaCent(dataset, grupos, cent):
    for i in range(len(cent)):
        for j in range(len(cent[i])):
            cent[i][j] = 0
        cont[i] = 0
    for i in range(len(grupos)):
        for j in range(len(dataset[i])):
            cent[grupos[i]][j] += dataset[i][j]
        cont[grupos[i]] += 1
    for i in range(len(cent)):
        for j in range(len(cent[i])):
            if cont[i] != 0:
                cent[i][j] /= cont[i]

def CalcDist(point, centroide):
    total = 0
    for i in range(m):
        total += (point[i] - centroide[i])**2
    return total

def CalculaGrupos(dataset, cent, grupos):
    continuar = False
    for ip in range(n):
        distMin = float("+inf")
        indexMin = float("+inf")
        for ic in range(K):
            dist = CalcDist(dataset[ip], cent[ic])
            if dist < distMin:
                distMin = dist
                indexMin = ic
        if grupos[ip] != indexMin:
            continuar = True
            grupos[ip] = indexMin
    return continuar



# def graph(dataset, cent, grupos):
#     colors = ['r', 'g', 'b', 'y', 'c', 'm']
#     for i in range(n):
#         pyplot.scatter(dataset[i][0], dataset[i][1], color = colors[grupos[i]])
#     for i in range(K):
#         pyplot.scatter(cent[i][0], cent[i][1], color = colors[i], marker = 'x')
#     pyplot.show()
#     return
#Graph no es necesario

if __name__ == "__main__":
    file = open("dataset.txt", "r")
    K = int(input("Numero de k: "))
    if K == 0:
        print('no puede ser 0')
        exit()
        
    # K = 9
    dataset = []
    respuesta = []
    index = []
    for linea in file:
        elem = linea.strip().split(" ")
        dataset.append(elem)
    file.close()
    cabecera = dataset.pop(0)
    cabecera.pop(0)
    cabecera.pop(-1)
  
    # n es el numero de renglones
    n = len(dataset)
    # m es el numero de columnas
    m = len(cabecera)
    
    for i in dataset:
        respuesta.append(i[-1])
        i.pop(-1)
    
    # elimino la primera y la ultima columna (index, respuesta)
        
    for i in dataset:
        index.append(i[0])
        i.pop(0)
        
    
    for i in range(n):
        for j in range(m):
            dataset[i][j-1] = int(dataset[i][j])
    dsT = list(zip(*dataset))
    cent = [[0 for _ in range(m)] for _ in range(K)]
        

    maxim, minim = maximMinim(dsT)
    for i in range(K):
        for j in range(m):
            cent[i][j] = random.randint(minim[j], maxim[j])
    grupos = [0 for i in range(n)]
    cont = [0 for i in range(K)] # ver

    continuar = True
    while continuar:
        continuar = CalculaGrupos(dataset, cent, grupos)
        ActualizaCent(dataset, grupos, cent)

    cont = [0 for _ in range(K)]
    prom = [0 for _ in range(K)]
    for i in range(n):
        prom[grupos[i]] += CalcDist(dataset[i], cent[grupos[i]])
        cont[grupos[i]] += 1

    for i in range(K):
        if cont[i] != 0:
            prom[i] = prom[i] / cont[i]
    promDistGlobal = numpy.average(prom)

    print("Promedio Distancia Global =", promDistGlobal)
    print("Centroides")
    for i in range(K):
        print(cent[i])
        
    # graph(dataset, cent, grupos)