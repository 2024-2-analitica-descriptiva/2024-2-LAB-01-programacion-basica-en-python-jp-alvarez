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
    with open("files/input/data.csv", mode="r", encoding="utf-8") as file:
        df = file.readlines()

    df = [row.split() for row in df]

    x = {}

    letterValue = [(row[3].split(","), row[1]) for row in df]

    for tuple in letterValue:
        for letter in tuple[0]:
            for i in letter:
                if letter in x:
                    x[letter] += int(tuple[1])
                else:
                    x[letter] = int(tuple[1])

    y = dict(sorted(x.items()))
    return y

print(pregunta_11())