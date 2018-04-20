import numpy as np
# PATRONES
a1 = [2, 1]
a2 = [0, -1]
a3 = [-2,1]
a4 = [0,2]
#VALORES ESPERADOS
valor_esperado=[1,1,-1,-1]

#ASIGNACION DE VIAS A LOS PATRONES DE ENTRADA
entradas = [a1, a2, a3,a4]
entradas_vias=[]
for i in range(len(entradas)):
    vias = []
    vias= [1]
    for j in range(len(entradas[i])):
        vias.append(int(entradas[i][j]))
    entradas_vias.append(vias)


