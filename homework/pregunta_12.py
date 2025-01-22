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
    with open("files/input/data.csv", mode="r", encoding="utf-8") as file:
        df = file.readlines()

    df = [row.split() for row in df]

    x = {}

    letterValue = [(row[0], row[4].split(",")) for row in df]

    for tuple in letterValue:
        for letter in tuple[1]:
            letter = int(letter.split(":")[1])
            if tuple[0] in x:
                x[tuple[0]] += int(letter)
            else:
                x[tuple[0]] = int(letter)

    y = dict(sorted(x.items()))
    return y

print(pregunta_12())
    
