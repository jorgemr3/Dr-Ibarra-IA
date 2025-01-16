# import random
def init():
    global arr, v1, v2, minimos
    # arr = [28,7,2,33,54,50,5,13,20,32] #vector de 10 numeros
    arr = [50,70,88,24,92,4,15,25]
    # arr = [random.randint(1, 100) for _ in range(10)] #vector de 10 numeros
    v1 = [] #numeros mas altos del vector ingresado 
    v2 = [] #el resto de numeros usados para serie de fibonacci  
    minimos = [] #numeros mas bajos del vector ingresado
    

if __name__ == '__main__':
    init()
    arr = sorted(arr)
    print(arr)

    # quiero checar si cada uno de los elementos es par, si no es lo elimino
    # for i in range(len(arr)):
    #     if arr[i] % 2 == 0:
    #         arr.remove(arr[i])
    # print(arr)

    while len(v1) < 5:
        temp = max(arr)
        v1.append(temp)
        arr.remove(temp)

    while len(minimos) < 5:
        temp = min(arr)
        minimos.append(temp)
        arr.remove(temp)
    print('minimos: ', minimos)

    # minimos = arr[:5]
    # v1 = arr[5:] # maximos
    while len(v2) < 5:
        if len(v2) == 0: 
            v2.append(minimos[0])
        else: v2.append(v2[len(v2)-1] + minimos[len(v2)])
    print('Salida 1 (Maximos)', v1)
    print('Salida 2', v2)

   

