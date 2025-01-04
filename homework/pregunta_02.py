"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    letras = {}
    with open('files/input/data.csv') as f:
        for line in f:
            letra = line.strip().split('\t')[0]
            if letra in letras:
                letras[letra] += 1
            else:
                letras[letra] = 1

    return sorted([(k, v) for k, v in letras.items()])

