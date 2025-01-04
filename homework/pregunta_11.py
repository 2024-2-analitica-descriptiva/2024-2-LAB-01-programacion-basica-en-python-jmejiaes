"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    diccionario = {}

    with open('files/input/data.csv') as f:
        for line in f:
            valor = line.strip().split('\t')[1]
            for letra in line.strip().split('\t')[3].split(','):
                if letra in diccionario:
                    diccionario[letra] += int(valor)
                else:
                    diccionario[letra] = int(valor)

    return {k: int(v) for k, v in diccionario.items()}