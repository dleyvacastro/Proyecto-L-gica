# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:55:36 2020

@author: dleyv
"""
from Letras import P
from Letras import Pinv
# import sys

# sys.setrecursionlimit(50000)

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

def Inorder(f):
    if f.right == None:
        return f.label
    elif f.label == '-':
        return f.label + Inorder(f.right)
    else:
        return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")" 
#--------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------Regla 1-----------------------------------------------------#
def regla1():
    inicial = 1
    inicial1 = 1
    inicial2 = 1
    formula = ""
    for h in range(6):
        for d in range(6):
            for m2 in range(7):
                if inicial:
                    formula1 = P(h,d,m2,Nhoras, Ndias, Nmaterias)
                    
                    for m1 in range(7):
                        if inicial1:
                            if m1 != m2:
                                formula2 = P(h,d,m1,Nhoras, Ndias, Nmaterias)
                                inicial1 = 0
                        else:
                            if m1 != m2:
                                formula2 += P(h,d,m1,Nhoras, Ndias, Nmaterias) + 'O'
                    formula = formula2 + '-' + formula1 +'>'
                    
                    inicial = 0
                else:
                    formula1 = P(h,d,m2,Nhoras, Ndias, Nmaterias)
                    for m1 in range(7):
                        if inicial2:
                            if m1 != m2:
                                formula2 = P(h,d,m1,Nhoras, Ndias, Nmaterias)
                                inicial2 = 0
                        else:
                            if m1 != m2:
                                formula2 += P(h,d,m1,Nhoras, Ndias, Nmaterias) + 'O'
                            
                    inicial2 = 1
                    formula += formula2 + '-' + formula1 + '>' + 'Y'
    return formula
#-------------------------------------Regla 2-----------------------------------------------------#
def regla2(i):
    inicial = 1
    # for d in range(6):
    #     for m3 in range(7):
    #         for h3 in range(6):
    #             for m2 in range(7):
    #                 for h2 in range(6):
    #                     for m1 in range(7):
    #                         for h1 in range(6):
    #                             if inicial:
    #                                 if(m1 != m2 or h1 != h2) and (m1 != m3 or h1 != h3) and (m2 != m3 or h2 != h3):
    #                                     formula = P(h3, d, m3, Nhoras, Ndias, Nmaterias) + P(h3, d, m3, Nhoras, Ndias, Nmaterias) + 'Y'
    #                                     formula += P(h1, d, m1, Nhoras, Ndias, Nmaterias) + 'Y'
    #                                     inicial = 0
    #                             else :
                                
    #                                 if(m1 != m2 or h1 != h2) and (m1 != m3 or h1 != h3) and (m2 != m3 or h2 != h3):
    #                                     formula += P(h3, d, m3, Nhoras, Ndias, Nmaterias) + P(h2, d, m2, Nhoras, Ndias, Nmaterias) + 'Y'
    #                                     formula += P(h3, d, m1, Nhoras, Ndias, Nmaterias) + 'Y' + 'O'
    for h3 in range(6):
        for m3 in range(7):
            for h2 in range(6):
                for m2 in range(7):
                    for h1 in range(6):
                        for m1 in range(7):
                            if inicial:
                                if(m1 != m2 or h1 != h2) and (m1 != m3 or h1 != h3) and (m2 != m3 or h2 != h3):
                                    formula = P(h3, i, m3, Nhoras, Ndias, Nmaterias) + P(h3, i, m3, Nhoras, Ndias, Nmaterias) + 'Y'
                                    formula += P(h1, i, m1, Nhoras, Ndias, Nmaterias) + 'Y'
                                    inicial = 0
                            else:
                                if(m1 != m2 or h1 != h2) and (m1 != m3 or h1 != h3) and (m2 != m3 or h2 != h3):
                                    formula += P(h3, i, m3, Nhoras, Ndias, Nmaterias) + P(h2, i, m2, Nhoras, Ndias, Nmaterias) + 'Y'
                                    formula += P(h3, i, m1, Nhoras, Ndias, Nmaterias) + 'Y' + 'O'
    return formula
# print(regla2())
#-------------------------------------Regla 2-----------------------------------------------------#
def regla3():
    inicial = 1
    for m in range(7):
        for d in range(6):
            if inicial:
                formula = P(2, d, m, Nhoras, Ndias, Nmaterias)
                inicial = 0
            else:
                formula += P(2, d, m, Nhoras, Ndias, Nmaterias) + 'O'
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
                            formula = P(h2, d2, i, Nhoras, Ndias, Nmaterias) + P(h1, d1, i, Nhoras, Ndias, Nmaterias) + 'Y'
                            
                            
                            inicial = 0
                    else:
                        if d1!=d2 or h1 != h2:
                            formula += P(h2, d2, i, Nhoras, Ndias, Nmaterias) + P(h1, d1, i, Nhoras, Ndias, Nmaterias) + 'Y' + 'O' 
    return formula

#--------------------------------------------------------------------------------------------------#
# print(Inorderp(String2Tree(P(1, 5, 6, Ndias, Nhoras, Nmaterias))))
# print("regla 1: ")    
# #print(Inorderp(String2Tree(regla1())))
Regla1I = Inorder(String2Tree(regla1()))
# print(Regla1I)
#print("regla 2:")
#print(Inorderp(String2Tree(regla2())))
# Regla2I = Inorderp(String2Tree(regla2(0)))
# print(Regla2I)
# print("regla 3: ")
#print(Inorderp(String2Tree(regla3())))
Regla3I = Inorder(String2Tree(regla3()))
# print(Regla3I)
# print("regla 4: ")
Regla4_0I = Inorder(String2Tree(regla4(0)))
print(Inorderp(String2Tree(regla1())))
Regla4_1I = Inorder(String2Tree(regla4(1)))
Regla4_2I = Inorder(String2Tree(regla4(2)))
Regla4_3I = Inorder(String2Tree(regla4(3)))
Regla4_4I = Inorder(String2Tree(regla4(4)))
Regla4_5I = Inorder(String2Tree(regla4(5)))
Regla4_6I = Inorder(String2Tree(regla4(6)))
Regla4I = Regla4_0I + Regla4_1I + 'Y'
Regla4I += Regla4_2I + 'Y' 
Regla4I += Regla4_3I + 'Y' 
Regla4I += Regla4_4I + 'Y'
Regla4I += Regla4_5I + 'Y' 
Regla4I += Regla4_6I + 'Y'  
# print(Regla4_0I)
# for i in range(7):
#     print("regla 4.{0}: ".format(i))
# #    print(Inorderp(String2Tree(regla4(i))))

R = Regla1I + Regla3I + 'Y'
R += Regla4I + 'Y'
