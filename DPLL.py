from Letras import letras

# LP = [chr(x) for x in range(256, 20000)]
LP = letras + [chr(x) for x in range(508, 50000)]
def Unidad(s):
    for i in s:
        if len(i) == 1:
            return i[0]

def Complemento(l):
    # print(l)
    if l in LP:
        return '-' + l
    elif l[1] in LP:
        return l[1]
    else:
        my_error = ValueError("ERROR")
        raise my_error

def unit_Propagate(s, i):
    unidad = Unidad(s)
    while ([] not in s) and (unidad != None):
        com = Complemento(unidad)
        s = [c for c in s if unidad not in c]
        for c in s:
            if com in c:
                c.remove(com)
        if unidad[0] == '-':
            i[com] = 0
        else:
            i[unidad] = 1
        unidad = Unidad(s)
    return s, i


def DPLL(s, i):
    s, i = unit_Propagate(s, i)
    if [] in s:
        return False, {}
    elif len(s) == 0:
        return True, i
    else:
        
        l = s[0][0]
        com = Complemento(l)
        s2 = [j[:] for j in s if l not in j]
        for x in s2:
            if com in x:
                x.remove(com)
        i2 = i
        if l[0] == '-':
            i2[com] = 0
        else:
            i2[l] = 1
            
        x, y = DPLL(s2, i2)
        if x == True:
            return True, i2
        else:
            s3 = [x[:] for x in s if com not in x]
            for x in s3:
                if l in x:
                    x.remove(l)
            i3 = i
            if l[0] == '-':
                i3[com] = 1
            else:
                i3[l] = 0
            return DPLL(s3, i3)
