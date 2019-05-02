chaEscolhido = int(input())
contar=0
chas = list(map(int, input().split()))
for i in range(len(chas)):
    if(chaEscolhido==chas[i]):
        contar+=1
print(contar)