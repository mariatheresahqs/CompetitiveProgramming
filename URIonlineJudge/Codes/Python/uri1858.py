nPessoas = int(input())
pessoas = [int(x) for x in input().split()]
menor = pessoas[0]
posicao = 0
for i in range(nPessoas):
    if(menor>pessoas[i]):
        menor = pessoas[i]
        posicao = i
print(posicao+1)