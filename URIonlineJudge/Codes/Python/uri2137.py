while True:
    try:
        nCasos = int(input())
        vetor = [int(input()) for x in range(nCasos)]

        for i in range(nCasos):
            for j in range(nCasos-1-i):
                if(vetor[j]>vetor[j+1]):
                    temporario = vetor[j]
                    vetor[j] = vetor[j+1]
                    vetor[j+1] = temporario

        for i in range(nCasos):
            if(vetor[i]<10):
                print("000{}".format(vetor[i]))
            elif(vetor[i]<100):
                print("00{}".format(vetor[i]))
            elif(vetor[i]<1000):
                print("0{}".format(vetor[i]))
            else:
                print("{}".format(vetor[i]))

    except EOFError:
        break