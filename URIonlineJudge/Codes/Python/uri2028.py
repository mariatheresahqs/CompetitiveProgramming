indice = 1

while True:
    try:
        valor = int(input())
        nCasos = 1
        vetor = []
        if(valor==0):
            vetor.append(valor)

        else:
            for i in range(0, valor+1, 1):
                vetor.append(i)


        for i in range(len(vetor)):
            for j in range(int(vetor[i])):
                nCasos+=1

        if (valor == 0):
            print("Caso {}: {} numero".format(indice, nCasos))
            print("0", end=" ")
            print()
        else:
            print("Caso {}: {} numeros".format(indice, nCasos))
            for i in range(0, len(vetor), 1):
                if (int(vetor[i]) == 0):
                    print("0", end=" ")
                for j in range(int(vetor[i])):
                    if(j==(vetor[i]-1) and i==(len(vetor)-1)):
                        print(vetor[i], end="")
                    else:
                        print(vetor[i], end=" ")
            print()
            print()
        indice +=1

    except EOFError:
        break