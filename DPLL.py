letrasProposicionales = ['p', 'q', 'r', 's', 't']


def unit_Propagate(s, i):
    unidad = hay_unidad(s)
    while ([] not in s) and (unidad != None):
        complementos = complemento(unidad)
        s = [c for c in s if unidad not in c]
        for c in s:
            if complementos in c:
                c.remove(complementos)
        if unidad[0] == '-':
            i[complementos] = 0
        else:
            i[unidad] = 1
        unidad = hay_unidad(s)
    return s, i

def complemento(letra):
    if letra in letrasProposicionales:
        return '-' + letra
    elif letra[0] == '-':
        return letra[1]
    else:
        raise Exception("error")

def hay_unidad(s):
    for i in s:
        if len(i) == 1:
            return i[0]
    return None

def DPLL(s, i):
    y = []
    s, i = unit_Propagate(s, i)
    if y in s:
        return "Insatisfacible", {}
    elif len(s) == 0:
        return "Satisfacible", i
    else:
        l = s[0][0]
        complementos = complemento(l)
        ss = [j[:] for j in s if l not in j]
        for x in ss:
            if complementos in x:
                x.remove(complementos)
        ii = i
        if l[0] == '-':
            ii[complementos] = 0
        else:
            ii[l] = 1
            
        a, b = DPLL(ss, ii)
        if a == "Satisfacible":
            return "Satisfacible", ii
        else:
            sss = [x[:] for x in s if complementos not in x]
            for x in sss:
                if l in x:
                    x.remove(l)
            iii = i
            if l[0] == '-':
                iii[complementos] = 1
            else:
                iii[l] = 0
            return DPLL(sss, iii)
        

a = [['p','q','r'], ['-p', '-q', '-r'], ['-p', 'q', 'r'], ['-q', 'r'], ['q', '-r']]
b = [[''],[],[],[]]
sol ={}
DPLL(a, sol)
print(sol)