"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    letras = {}
    with open('files/input/data.csv') as f:
        for line in f:
            letra = line.strip().split('\t')[0]

            for par in line.strip().split('\t')[4].split(','):
                numero = int(par.split(':')[1])

                if letra in letras:
                    letras[letra] += numero
                else:
                    letras[letra] = numero

    return letras