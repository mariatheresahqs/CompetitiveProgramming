import math

nCasos = int(input())
for i in range(nCasos):
    teste = 0
    valor = int(input())
    parada = (int)(math.sqrt(valor))
    if(valor<=2):
        if(valor==0):
            print("Not Prime")
        if(valor==1):
            print("Not Prime")
        if(valor==2):
            print("Prime")
    else:
        for j in range(2, parada+1, 1):
            if(valor%j==0):
                teste+=1
            if(teste==2):
                break
        if(teste>=1):
            print("Not Prime")
        else:
            print("Prime")
        # print(valor)