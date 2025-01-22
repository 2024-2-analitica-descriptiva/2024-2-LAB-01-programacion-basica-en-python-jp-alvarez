"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", mode= "r", encoding='utf-8') as file:
        df = file.readlines()

    df = [row.split() for row in df]

    x = {}

    tuplasletters = [(row[0], int(row[1])) for row in df]

    for tupla in tuplasletters:
        if tupla[0] in x:
            x[tupla[0]].append(tupla[1])
        else:
            x[tupla[0]] = [tupla[1]]

    y = [(key, max(value), min(value)) for key, value in x.items()]
    y.sort()

    return y

print(pregunta_05())