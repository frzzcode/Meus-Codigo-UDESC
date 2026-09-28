lista = [1,4,7,2,5]

def booblesort(lista):
    for i in range(len(lista)):
        for j in len(lista):
            if lista[j] <= lista[j+1]:
                lista[j] = lista[j+1]
            else:
                continue
            