"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """


    with open("files/input/data.csv", mode= "r", encoding='utf-8') as file:
        df = file.readlines()
    
    df = [row.split() for row in df]

    col = [int(row[1]) for row in df]

    suma = sum(col)

    return suma

print(pregunta_01())