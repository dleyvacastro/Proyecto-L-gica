  
# -*- coding: utf-8 -*-

# Transformación de una formula en forma clausal
# Input: cadena de la formula en notacion inorder
# Output: lista de listas de literales

# Importando la libreria FNC
import FNC as fn
import Reglas 
letrasProposicionalesA = [chr(x) for x in range(256, 600)]
# # Formula a la cual encontrar su forma clausal
# formula = "-p"
# formula = "(pYq)"
# formula = "(pOq)"
print(Reglas.regla3())
formula = Reglas.regla3()

# Aplicando el algoritmo de Tseitin a formula
# Se obtiene una cada que representa la formula en FNC
fFNC = fn.Tseitin(formula, letrasProposicionalesA)

# Se obtiene la forma clausal como lista de listas de literales
fClaus = fn.formaClausal(fFNC)

# Imprime el resultado en consola
print(fClaus)
