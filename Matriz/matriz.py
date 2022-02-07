import random
m = [
    [11,2,3,4,5],
    [2,3,3,4,7],
    [1,4,3,4,7],
    [14,5,3,4,7],
    [1,2,3,4,7]
    ]
def matriz():
    """
    testing generar matriz
    >>> random.seed(1)
    >>> matriz()
    [[3, 10, 2, 5, 2], [8, 8, 8, 7, 4], [2, 8, 1, 7, 7], [10, 1, 8, 5, 4], [10, 2, 6, 1, 1]]
    """
    matriz = []
    for i in range(0,5):
        matriz.append([])
        for j in range(0,5):
            matriz[i].append(random.randint(1,10))
    return matriz

def es_consecutivo(lista):
    """
    Testing consecutivo
    >>> es_consecutivo([1,2,3,4,6])
    [1, 4]
    
    Testing consecutivo
    >>> es_consecutivo([0,2,3,4,5])
    [2, 5]

    Testing no es consecutivo
    >>> es_consecutivo([0,22,3,14,5])
    []
    """
    if lista[0]+1 == lista[1] and lista[1]+1 == lista[2] and lista[2]+1 == lista[3]:
        return [1,4]
    elif lista[1]+1 == lista[2] and lista[2]+1 == lista[3] and lista[3]+1 == lista[4]:
        return [2,5]
    else:
        return []

def buscar_secuencia(matriz):
    """
    Testing encontrar secuencia
    >>> buscar_secuencia(m)
    [11, 2, 3, 4, 5]
    [2, 3, 3, 4, 7]
    [1, 4, 3, 4, 7]
    [14, 5, 3, 4, 7]
    [1, 2, 3, 4, 7]
    Existe una secuencia entre fila: 5 columna: 1  y fila: 5 columna: 4
    Existe una secuencia entre columna: 2 fila: 1  y columna: 2 fila: 4

    Testing no existe secuencia
    >>> random.seed(1)
    >>> buscar_secuencia(matriz())
    [3, 10, 2, 5, 2]
    [8, 8, 8, 7, 4]
    [2, 8, 1, 7, 7]
    [10, 1, 8, 5, 4]
    [10, 2, 6, 1, 1]
    No existen secuencias!
    
    """
    res_fila = []
    res_columna=[]
    for fila in range(len(matriz)):
        print(matriz[fila])
        if es_consecutivo(matriz[fila]):
            res_fila = [fila+1,es_consecutivo(matriz[fila])]
        lista_col = []
        for columna in range(len(matriz[0])): 
            lista_col .append(matriz[columna][fila])
        if es_consecutivo(lista_col):
            res_columna = [fila+1,es_consecutivo(lista_col)]
    if res_fila:
        print("Existe una secuencia entre fila:",res_fila[0],"columna:",res_fila[1][0]," y fila:",res_fila[0],"columna:",res_fila[1][1])
    if res_columna:
        print("Existe una secuencia entre columna:",res_columna[0],"fila:",res_columna[1][0]," y columna:",res_columna[0],"fila:",res_columna[1][1])
    elif not res_columna and not res_fila:
        print("No existen secuencias!")

if __name__=='__main__':
    import doctest
    doctest.testmod()




