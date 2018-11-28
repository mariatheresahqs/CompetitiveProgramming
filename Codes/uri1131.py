iniciar = 1
golint=0
golgre=0
jogo=0
vitint=0
vitgre=0
empate=0

while (iniciar==1):
    iniciar = 0
    gols = [int(x) for x in input().split()]
    if (gols[0]>gols[1]):
        vitint+=1
    elif (gols[1]>gols[0]):
        vitgre+=1
    else:
        empate+=1
    golint+= gols[0]
    golgre+= gols[1]
    jogo+=1
    print("Novo grenal (1-sim 2-nao)")
    iniciar = int(input())
    if (iniciar==2):
        print("{} grenais".format(jogo))
        print("Inter:{}".format(vitint))
        print("Gremio:{}".format(vitgre))
        print("Empates:{}".format(empate))
        if (vitint>vitgre):
            print("Inter venceu mais")
        else:
            print("Gremio venceu mais")
        break
