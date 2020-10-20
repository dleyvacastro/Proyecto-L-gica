# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:08:31 2020

@author: dleyv
"""


def codifica(d, h, Nd, Nh):
#    assert(d>=0 and d <= Nd), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nd - 1)  + "\nSe recibio " + str(d)
    assert(h>=0 and h <= Nh), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nh - 1)  + "\nSe recibio " + str(h)
    
    n = Nd * h +d
    return n

def decodifica(n, Nd, Nh):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla
 #   assert((n >= 0) and (n <= Nd * Nh - 1)), 'Codigo incorrecto! Debe estar entre 0 y' + str(Nd * Nh - 1) + "\nSe recibio " + str(n)
    h = int(n / Nh)
    d = n % Nh
    return h, d


Nmaterias = 7
Ngrupo = 2
Ndias = 6
Nhoras = 6


def P(m, d, h, Nm, Nd, Nh):
    assert((m >= 0) and (m <= Nm - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nm - 1) + "\nSe recibio " + str(m)
#    assert((g >= 0) and (g <= Ng - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Ng - 1) + "\nSe recibio " + str(g)
    assert((d >= 0) and (d <= Nd - 1)), 'Tercer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nd - 1)  + "\nSe recibio " + str(d)
    assert((h >= 0) and (h <= Nh - 1)), 'Cuarto argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nh - 1)  + "\nSe recibio " + str(h)

    v1 = codifica(h, d, Nhoras, Ndias)
    v2 = codifica(v1, m, Nhoras * Ndias, Nmaterias)
    codigo = chr(256+v2)
    return codigo
    
def Pinv(codigo, Nh, Nd, Nm):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    x = ord(codigo) - 256
    v1, m = decodifica(x, Nd * Nh, Nm)
    h, d = decodifica(v1, Nh, Nd)
    return h, d, m

print(u"Números correspondientes a la codificación:")
print("\nhoras x dias")
for i in range(Nhoras):
    for j in range(Ndias):
        v1 = codifica(i, j, Nhoras, Ndias)
        print(v1, end = " ")
    print("")
for v1 in range(6*6):
    f, c = decodifica(v1, Nhoras, Ndias)
    print('Código: '+str(v1)+', Hora: '+str(f)+', Dia: '+str(c))


letras = []

for k in range(Nmaterias):
    print("Numero: "+str(k))
    print("filas x columnas")
    for i in range(Nhoras):
        for j in range(Ndias):
            cod = P(i, j, k, Nhoras, Ndias, Nmaterias)
            print(cod, end = " ")
            letras.append(cod)
        print("")
    print('\n')

for cod in letras:
    print('Letra = '+cod, end=', ')
    m, d, h = Pinv(cod, Nmaterias, Ndias, Nhoras)
    print('Materia = '+str(m), end=', ')
    print('Dia = '+str(d), end=', ')
    print('Hora = '+str(h))
print(len(letras))
#-------------------------------------------------------------------------------------------------------------#
    