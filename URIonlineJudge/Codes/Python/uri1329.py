while True:
    casos = int(input())
    joao = 0
    maria = 0
    if(casos == 0):
        break
    else:
        vetor = list(map(int, input().split()))
        for i in range(casos):
            if(vetor[i]==0):
                maria+=1
            else:
                joao+=1
        print("Mary won {} times and John won {} times".format(maria, joao))

