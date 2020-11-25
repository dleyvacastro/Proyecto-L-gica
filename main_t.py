  
# -*- coding: utf-8 -*-

# Transformación de una formula en forma clausal
# Input: cadena de la formula en notacion inorder
# Output: lista de listas de literales

# Importando la libreria FNC
import FNC as fn
import Reglas 
import Letras
letrasProposicionalesA = Letras.letras
# # Formula a la cual encontrar su forma clausal
# formula = "-p"
# formula = "(pYq)"
# formula = "(pOq)"
#print(Reglas.regla3())
R1 = Reglas.Regla1I
R3 = Reglas.Regla3I
R4_0 = Reglas.Regla4_0I
R4_1 = Reglas.Regla4_1I
R4_2 = Reglas.Regla4_2I
R4_3 = Reglas.Regla4_3I
R4_4 = Reglas.Regla4_4I
R4_5 = Reglas.Regla4_5I
R4_6 = Reglas.Regla4_6I
R = '(' + R1 + 'Y' + R3 + 'Y' + R4_0 + 'Y' + R4_1 + 'Y' + R4_2 + 'Y' + R4_3 + 'Y' + R4_4 + 'Y' + R4_5 + 'Y' + R4_6 + ')'

# Aplicando el algoritmo de Tseitin a formula
# Se obtiene una cada que representa la formula en FNC
# fFNC_R1 = fn.Tseitin(R1, letrasProposicionalesA)
# #fFNC_R2 = fn.Tseitin(R2, letrasProposicionalesA)
# fFNC_R3 = fn.Tseitin(R3, letrasProposicionalesA)
# fFNC_R1_0 = fn.Tseitin(R4_0, letrasProposicionalesA)
# fFNC_R1_1 = fn.Tseitin(R4_1, letrasProposicionalesA)
# fFNC_R1_2 = fn.Tseitin(R4_2, letrasProposicionalesA)
# fFNC_R1_3 = fn.Tseitin(R4_3, letrasProposicionalesA)
# fFNC_R1_4 = fn.Tseitin(R4_4, letrasProposicionalesA)
# fFNC_R1_5 = fn.Tseitin(R4_5, letrasProposicionalesA)
# fFNC_R1_6 = fn.Tseitin(R4_6, letrasProposicionalesA)
fFNC_R = fn.Tseitin(R, letrasProposicionalesA)


# Se obtiene la forma clausal como lista de listas de literales
# fClaus_R1 = fn.formaClausal(R1)
# fClaus_R1 = fn.formaClausal(R2)
# fClaus_R1 = fn.formaClausal(R3)
# fClaus_R4_0 = fn.formaClausal(R4_0)
# fClaus_R4_1 = fn.formaClausal(R4_1)
# fClaus_R4_2 = fn.formaClausal(R4_2)
# fClaus_R4_3 = fn.formaClausal(R4_3)
# fClaus_R4_4 = fn.formaClausal(R4_4)
# fClaus_R4_5 = fn.formaClausal(R4_5)
# fClaus_R4_6 = fn.formaClausal(R4_6)
fClaus_R = fn.formaClausal(fFNC_R)

