import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox

print("Listo")

fig, axes = plt.subplots()
axes.get_xaxis().set_visible(False)
axes.get_yaxis().set_visible(False)

horizontal_step = 1./7
vertical_step = 1./6
tangulos = list()

for i in range(7):
    tangulos.append(patches.Rectangle((i*horizontal_step, 3*vertical_step), horizontal_step, vertical_step, facecolor='black'))

for t in tangulos:
    axes.add_patch(t)

fig.savefig("horario1.png")
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
