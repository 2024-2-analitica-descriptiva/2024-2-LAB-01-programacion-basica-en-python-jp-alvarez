"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    with open ("files/input/data.csv", mode="r", encoding="utf-8") as file:
        df = file.readlines()

    df = [row.split() for row in df]

    x = {}

    letterV = [(row[0], row[1]) for row in df]

    for tuple in letterV:
        key = tuple[0]
        value = int(tuple[1])
        if value not in x:
            x[value] = [key]
        else:
            x[value].append(key)


    y = [(key, value) for key, value in x.items()]
    y.sort()

    return y

print(pregunta_07())
    

