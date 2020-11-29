import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox
from modelaje import modelo

print("Listo")

def horario(modelo):
    colores = {0: "red", 1: "blue", 2: "green", 3: "grey", 4: "yellow", 5: "purple"}
    
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    axes.invert_yaxis()

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
    
# modelo = {("Algoritmos", 0, 1): 1, ("Fundamentos", 0, 3): 1, ("Lógica", 1, 0): 1, ("Análisis", 2, 0): 1, ("Fundamentos", 2, 3): 1, \
#           ("Cálculo", 2, 4): 1, ("Lógica", 3, 0): 1, ("Algoritmos", 3, 3): 1, ("Cálculo", 4, 0): 1, ("Cívica", 4, 1): 1, \
#           ("Cálculo", 4, 4): 1, ("Algoritmos", 5, 1): 1}
