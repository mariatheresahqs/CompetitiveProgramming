vetor = [int(i) for i in input().split()]
maior = 0
for j in range(len(vetor)):
    if(vetor[j]>maior):
        maior = vetor[j]
print(maior)
