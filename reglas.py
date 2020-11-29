"""
# Las clases no se pueden cruzar
def regla1(modelo):
    modelo_n = []
    new_modelo = {}
    for key in modelo.keys():
        dia = key[1]
        hora = key[2]
        if (dia, hora) not in modelo_n:
            modelo_n.append((dia, hora))
            new_modelo[key] = modelo[key]
    return new_modelo
"""
from random import randint

# Máximo tres clases por dia
def regla2(modelo):
    dias = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key in modelo.keys():
        dias[key[1]].append(key)
    #print(dias[0])
    del modelo
    modelo = {}
    for key in dias.keys():
        length = dias[key].__len__()
        one, two, three = randint(0, length-2), randint(0, length-2), randint(0, length-2)
        while one==two or one==three or two==three or dias[key][one][2]==dias[key][two][2] or dias[key][two][2]==dias[key][three][2] or \
        dias[key][one][2]==dias[key][three][2] or dias[key][one][0]==dias[key][two][0] or dias[key][one][0]==dias[key][three][0] or \
        dias[key][two][0]==dias[key][three][0]:
            one, two, three = randint(0, length-2), randint(0, length-2), randint(0, length-2)
        first, second, third = dias[key][one], dias[key][two], dias[key][three]
        dias[key] = [first, second, third]
    for value in dias.values():
        for element in value:
            modelo[element] = 1
    return modelo
    """
        if dias[key[1]].__len__()<3:
    for key in modelo.keys():
            dias[key[1]].append(key)
    del modelo
    modelo = {}
    for key in dias.keys():
        for element in dias[key]:
            modelo[element] = 1
    return modelo"""

# NO hay clase a las 12
def regla3(modelo):
    almuerzo = []
    for key in modelo.keys():
        if key[2]==3:
            almuerzo.append(key)
    for element in almuerzo:
        modelo.pop(element)
    return modelo
"""
# Solo dos sesiones de cada materia por semana
def regla4(modelo):
    clases = set()
    for keys in modelo.keys():
        clases.add(keys[0])
    print(clases)
"""
