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
print("VECTOR DE ENTRADA AGREGANDO  VIAS")

for i in range(len(entradas)):
    vias = []
    vias= [1]
    for j in range(len(entradas[i])):
        vias.append(int(entradas[i][j]))
    entradas_vias.append(vias)
    print(entradas_vias[i])

print("VALOR ESPERADO")
print(valor_esperado)
#ARREGLO DE LA MATRIZ "ALEATORIA"
alpha=1
vector_pesos=[0.5,-0.7,0.2]
matriz_pesos=np.array(vector_pesos).reshape(len(entradas_vias[0]),1)
salida=0
salida_final=0
correcto=False
i=0
errores=[]
while(correcto!=True):
    for j in range(len(entradas_vias[i])):
            salida=entradas_vias[i][j]*vector_pesos[j]
            salida_final=salida_final+salida

    if(salida_final>=0):
        salida_final=1
    else:
        salida_final=-1
    error=valor_esperado[i]-salida_final
    if (error==0):
        errores.append(error)
        if(i==len(entradas_vias)-1):
            print("MATRIZ PESOS")
            print(matriz_pesos)
            print("Errores")
            print(errores)
            correcto=True
        i = i + 1

    else:
        for k in range(len(entradas_vias[i])):
            vector_pesos[k]=vector_pesos[k]+(alpha*error)*entradas_vias[i][k]
        errores.append(error)
        matriz_pesos = np.array(vector_pesos).reshape(len(entradas_vias[i]),1)
        i=0