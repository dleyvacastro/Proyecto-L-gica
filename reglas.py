# Las clases no se pueden cruzar
def regla1(modelo):
    for key in modelo.keys():
        dia = key[1]
        hora = key[2]
        for other in modelo.keys():
            if other != key and key[1]==other[1] and key[2]==other[2]:
                modelo.pop(other)
    return modelo

# Máximo tres clases por dia
def regla2(modelo):
    dias = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    modelo_n = {}
    for key in modelo.keys():
        if dias[key[1]]<3:
            modelo_n[key] = 1
            dias[key[1]] += 1
        else:
            for comp in modelo.keys():
                if key!=comp:
                    modelo.pop(comp)
    return modelo

# NO hay clase a las 12
def regla3(modelo):
    for key in modelo.keys():
        if key[2]==2:
            modelo.pop(key)
    return modelo

# Solo dos sesiones de cada materia por semana
def regla4(modelo):
    clases = set()
    for key in modelo.keys():
        clases.add(key[0])
    semana = {}
    for element in clases:
        semana[element] = 0
    del clases
    for key in modelo.keys():
        if semana[key[0]]<2:
            semana[key[0]] += 1
        else:
            for comp in modelo.keys():
                if key!=comp:
                    modelo.pop(comp)
    return modelo
