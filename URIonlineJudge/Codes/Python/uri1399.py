qntElementos, processos, valor = map(int, input().split())
vetorElementos = []
contador = 0

for i in range(qntElementos):
    vetorElementos.append(int(input()))
# print(vetorElementos)
for j in range(processos):
    minimo, maximo, base, indiceElemento = map(int, input().split())

for k in range(minimo-1, maximo, 1):
    if(vetorElementos[k]<base):
        contador+=1
    # print(valor, contador, maximo, minimo)
    vetorElementos[indiceElemento-1] = (valor*contador)//(maximo-minimo+1)

for i in range(qntElementos):
    print(vetorElementos[i])