LP = [chr(x) for x in range(97, 123)]
print(LP)

def hay_unidad(s):
    for i in s:
        if len(i) == 1:
            return i[0]
    return None

def complemento(l):
    if l in LP:
        return '-' + l
    elif l[0] == '-':
        return l[1]
    else:
        my_error = ValueError("ERROR")
        raise my_error

def unit_Propagate(s, i):
    unidad = hay_unidad(s)
    while ([] not in s) and (unidad != None):
        com = complemento(unidad)
        s = [c for c in s if unidad not in c]
        for c in s:
            if com in c:
                c.remove(com)
        if unidad[0] == '-':
            i[com] = 0
        else:
            i[unidad] = 1
        unidad = hay_unidad(s)
    return s, i


def DPLL(s, i):
    y = []
    s, i = unit_Propagate(s, i)
    if y in s:
        return False, {}
    elif len(s) == 0:
        return True, i
    else:
        
        l = s[0][0]
        com = complemento(l)
        s2 = [j[:] for j in s if l not in j]
        for x in s2:
            if com in x:
                x.remove(com)
        i2 = i
        if l[0] == '-':
            i2[com] = 0
        else:
            i2[l] = 1
            
        a, b = DPLL(s2, i2)
        if a == True:
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
        

a = [['p','q','r'], ['-p', '-q', '-r'], ['-p', 'q', 'r'], ['-q', 'r'], ['q', '-r']]
b = [['p','q','r','-s'],['p','t','s'],['-p','-q'],['p','r','-q','-s']]
c = [['p','q','-r'],['r','s','t'],['t'],['p','s'],['q','-p']]
d = [['p','-q'], ['-p','-q'],['q','r'],['-q','-r'],['-p','-r'],['p','-r']]
e = [['r','p','s'],['-r','-p','s'],['-r','p','s'],['p','-s']]
sol ={}
x, y = DPLL(e, sol)
print(x)
if x:
    print(y)