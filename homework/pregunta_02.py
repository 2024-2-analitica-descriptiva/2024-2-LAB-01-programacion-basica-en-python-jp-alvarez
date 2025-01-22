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
    with open("files/input/data.csv", mode= "r", encoding='utf-8') as file:
        df = file.readlines()

    df = [row.split() for row in df]

    letters = [row[0] for row in df]

    x = {}

    for letter in letters:
        if letter in x:
            x[letter] += 1
        else:
            x[letter] = 1

    y = list(x.items())

    y.sort()

    return y

print(pregunta_02())