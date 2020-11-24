# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:55:36 2020

@author: dleyv
"""
from Letras import P
from Letras import Pinv

Nmaterias = 7
Ndias = 6
Nhoras = 6

class Tree(object):
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label

def String2Tree(A):
    letrasProposicionales=[chr(x) for x in range(256, 600)]
    Conectivos = ['O','Y','>','=']
    Pila = []
    for c in A:
        if c in letrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c=='-':
            FormulaAux = Tree(c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree(c,Pila[-1],Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
        else:
            print(u"Hay un problema: el símbolo " + str(c)+ " no se reconoce")
    return Pila[-1]

def Inorderp(f):
    if f.right == None:
        return str(Pinv(f.label, Nhoras, Ndias, Nmaterias))
    elif f.label == '-':
        return f.label + Inorderp(f.right)
    else:
        return "(" + Inorderp(f.left) + f.label + Inorderp(f.right) + ")"
    
#--------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------Regla 1-----------------------------------------------------#
def regla1():
    inicial = 1
    inicial1 = 1
    formula = ""
    for m2 in range(7):
        for d2 in range(6):
            for h2 in range(6):
                if inicial:
                    formula1 = P(m2,d2,h2,Nmaterias, Ndias, Nhoras)
                    
                    for m1 in range(7):
                        if inicial1:
                            if m1 != m2:
                                formula2 = P(m1,d2,h2,Nmaterias, Ndias, Nhoras)
                                inicial1 = 0
                        else:
                            if m1 != m2:
                                formula2 += P(m1,d2,h2,Nmaterias, Ndias, Nhoras) + 'O'
                    formula = formula2 + '-' + formula1 +'>'
                    
                    inicial = 0
                else:
                    formula1 = P(m2,d2,h2,Nmaterias, Ndias, Nhoras)
                    for m1 in range(1,7):
                        if inicial1:
                            if m1 != m2:
                                formula2 = P(m1,d2,h2,Nmaterias, Ndias, Nhoras)
                                inicial1 = 0
                        else:
                            if m1 != m2:
                                formula2 += P(m1,d2,h2,Nmaterias, Ndias, Nhoras) + 'O'
                    inicial1 = 1
                    formula += formula2 + '-' + formula1 + '>' + 'Y'
                    
    return formula
#-------------------------------------Regla 2-----------------------------------------------------#
def regla2():
    inicial = 1
    for d in range(6):
        
        for m3 in range(7):
            for d3 in range(6):
                for h3 in range(6):
                    for m2 in range(7):
                        for d2 in range(6):
                            for h2 in range(6):
                                for m1 in range(7):
                                    for d1 in range(6):
                                        for h1 in range(6):
                                            if inicial:
                                                if (m1!=m2 or d1 != d2 or h1 != h2) and (m1!=m3 or d1 != d3 or h1 != h3) and (m2!=m3 or d2 != d3 or h2 != h3):
                                                    formula = P(m3, d3, h3, Nmaterias, Ndias, Nhoras) + P(m2, d2, h2, Nmaterias, Ndias, Nhoras) + 'Y'
                                                    formula += P(m1, d1, h1, Nmaterias, Ndias, Nhoras) + 'Y'
                                                    inicial = 0
                                            else:
                                                if (m1!=m2 or d1 != d2 or h1 != h2) and (m1!=m3 or d1 != d3 or h1 != h3) and (m2!=m3 or d2 != d3 or h2 != h3):
                                                     formula += P(m3, d3, h3, Nmaterias, Ndias, Nhoras) + P(m2, d2, h2, Nmaterias, Ndias, Nhoras) + 'Y'
                                                     formula += P(m1, d1, h1, Nmaterias, Ndias, Nhoras) + 'Y' +'O'
    return formula
#print(len(regla2()))
#-------------------------------------Regla 2-----------------------------------------------------#
def regla3():
    inicial = 1
    for m in range(7):
        for d in range(6):
            if inicial:
                formula = P(m, d, 2, Nmaterias, Ndias, Nhoras)
                inicial = 0
            else:
                formula += P(m, d, 3, Nmaterias, Ndias, Nhoras) + 'O'
    formula += '-'
    return formula
#-------------------------------------Regla 4-----------------------------------------------------#
def regla4(i):
    inicial = 1
    for d2 in range(6):
        for h2 in range(6):
            for d1 in range(6):
                for h1 in range(6):
                    if inicial:
                        if d1!=d2 or h1 != h2:
                            formula = P(i, d2, h2, Nmaterias, Ndias, Nhoras) + P(i, d1, h1, Nmaterias, Ndias, Nhoras) + 'Y'
                            inicial = 0
                    else:
                        if d1!=d2 or h1 != h2:
                            formula += P(i, d2, h2, Nmaterias, Ndias, Nhoras) + P(i, d1, h1, Nmaterias, Ndias, Nhoras) + 'Y' + 'O'
    return formula

#--------------------------------------------------------------------------------------------------#

print("regla 1: ")    
print(Inorderp(String2Tree(regla1())))
print("regla 2:")
#print(Inorderp(String2Tree(regla2())))
print("regla 3: ")
print(Inorderp(String2Tree(regla3())))
print("regla 4: ")
for i in range(7):
    print("regla 4.{0}: ".format(i))
    print(Inorderp(String2Tree(regla4(i))))
    