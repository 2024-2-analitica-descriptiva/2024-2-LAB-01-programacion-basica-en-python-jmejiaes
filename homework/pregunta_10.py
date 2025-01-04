"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    letras = []
    with open('files/input/data.csv') as f:
        for line in f:
            letra, valor1, valor2 = line.strip().split('\t')[0], int(len(line.strip().split('\t')[3].split(','))), int(len(line.strip().split('\t')[4].split(',')))
            letras.append((letra, valor1, valor2))

    return letras