import main_t, DPLL
from Reglas import Pinv
from Letras import letras

Nmaterias = 7
Ndias = 6
Nhoras = 6

modelo = open("modelo.txt", "w")

model = {}
sol = {}
x, y = DPLL.DPLL(main_t.fClaus_R1, sol)
print(y)
for i in y:
    if y[i] == 1 and i in letras:
        d, h, m = Pinv(i, Nhoras, Ndias, Nmaterias)
        if m == 0:
            m = "Cálculo" 
        elif m == 1:
            m = "Algoritmos"
        elif m == 2:
            m = "Fundamentos"
        elif m == 3:
            m = "Análisis"
        elif m == 4:
            m = "Cívica"
        elif m == 5:
            m = "Lógica"
        elif m == 6:
            m = "Electiva"
        model[(h, d, m)] = 1
        
print(model)

modelo.write(str(model))

modelo.close()