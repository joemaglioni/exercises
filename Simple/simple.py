import random
import math

def crear_lista():
    """
    Testing crear lista
    >>> random.seed(1)
    >>> crear_lista()
    [{'id': 1, 'edad': 18}, {'id': 2, 'edad': 73}, {'id': 3, 'edad': 98}, {'id': 4, 'edad': 9}, {'id': 5, 'edad': 33}, {'id': 6, 'edad': 16}, {'id': 7, 'edad': 64}, {'id': 8, 'edad': 98}, {'id': 9, 'edad': 58}, {'id': 10, 'edad': 61}]
    """

    lista = []
    for i in range(1,11):
        lista.append({"id":i,"edad":random.randint(1,100)})

    return lista

def ordenar(lista):

    """
    Testing ordenar lista
    >>> ordenar(lista=crear_lista())
    ID de la persona mas joven 6
    ID de la persona mas vieja 10
    [{'id': 10, 'edad': 98}, {'id': 1, 'edad': 84}, {'id': 9, 'edad': 78}, {'id': 5, 'edad': 63}, {'id': 8, 'edad': 56}, {'id': 7, 'edad': 50}, {'id': 2, 'edad': 49}, {'id': 3, 'edad': 27}, {'id': 4, 'edad': 13}, {'id': 6, 'edad': 4}]
    
    """

    def edad(x):
        return x["edad"]
    lista.sort(reverse=True,key=edad,)
    print("ID de la persona mas joven",lista[len(lista)-1]["id"])
    print("ID de la persona mas vieja",lista[0]["id"])
    return lista



if __name__ == '__main__':
    
    import doctest
    doctest.testmod()