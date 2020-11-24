import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox

print("Listo")

def horario(modelo):
    colores = {"Cálculo": "red", "Algoritmos": "blue", "Fundamentos": "green", "Análisis": "grey", "Cívica": "yellow", "Lógica": "purple"}
    
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    horizontal_step = 1./7
    vertical_step = 1./6
    tangulos = list()

    for i in range(7):
        tangulos.append(patches.Rectangle((i*horizontal_step, 3*vertical_step), horizontal_step, vertical_step, facecolor='black'))
        
    for key in modelo.keys():
        tangulos.append(patches.Rectangle((key[1]*horizontal_step, (key[2]+1)*vertical_step), horizontal_step, vertical_step, facecolor=colores[key[0]]))

    for t in tangulos:
        axes.add_patch(t)

    fig.savefig("horario1.png")
    
modelo = {("Algoritmos", 0, 1): 1, ("Fundamentos", 0, 3): 1, ("Lógica", 1, 0): 1, ("Análisis", 2, 0): 1, ("Fundamentos", 2, 3): 1, \
          ("Cálculo", 2, 4): 1, ("Lógica", 3, 0): 1, ("Algoritmos", 3, 3): 1, ("Cálculo", 4, 0): 1, ("Cívica", 4, 1): 1, \
          ("Cálculo", 4, 4): 1, ("Algoritmos", 5, 1): 1}

horario(modelo)
"""
def tablero(f, n):
    days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    colors = {"Calculo": "red", "Fundamentos": "blue", "Algoritmos": "green", "Lógica": "black", "Cívica": "grey", "Argumentos": "purple", "Electiva": "orange"}
    time = {7:1, 8:2, 9:3, 10:4, 11:5, 12:6, 13:7, 14:8, 15:9, 16:10, 17:11, 18:12}

    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    vertical = 1./13
    horizontal = 1./7
    count = 0
    tangulos = []

    for i in range(13):
        for l in range(7):
            tangulos.append(patches.Rectangle((i*horizontal, (j+1)*vertical), horizontal, vertical, angle=0.0, facecolor="transparent")

    for i in range(7):
        ver = i*horizontal
        tangulos.append(patches.Rectangle((0, ver), 0.005, 1, angle=0.0, facecolor="black"))

    for i in range(13):
        hor = i*horizontal
        tangulos.append(patches.Rectangle((hor, 0), 1, 0.005, angle=0.0, facecolor="black"))

    for t in tangulos:
        axes.add_patch(t)

    fig.savefig("horario_"+n+".png")
"""
