"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open("files/input/data.csv", mode= "r", encoding='utf-8') as file:
        df = file.readlines()

    df = [row.split() for row in df]    

    x = {}

    coldict = [row[4].split(",") for row in df]

    for row in coldict:
        for item in row:
            key, value = item.split(":")
            if key in x:
                x[key] += 1
            else:
                x[key] = 1
    
    y = dict(sorted(x.items()))
    return y

print(pregunta_09())
