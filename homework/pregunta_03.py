"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open("files/input/data.csv", mode= "r", encoding='utf-8') as file:
        df = file.readlines()

    df = [row.split() for row in df]

    x = {}

    tuplasletters = [(row[0], int(row[1])) for row in df]

    for tupla in tuplasletters:
        if tupla[0] in x:
            x[tupla[0]] += tupla[1]
        else:
            x[tupla[0]] = tupla[1]

    y = list(x.items())
    y.sort()

    return y

print(pregunta_03())