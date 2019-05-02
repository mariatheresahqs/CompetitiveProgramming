nPecas = int(input())
jogo = []
for i in range(nPecas):
    jogo.append(i+1)
# print(jogo)
pecas = list(map(int, input().split()))
faltando = 0
# print(nPecas, pecas)
pecas.sort()
# print(pecas)

for i in range(0, nPecas-1, 1):
    if(pecas[i]!=jogo[i]):
        faltando = i+1
        break
    else:
        faltando = nPecas
print(faltando)
