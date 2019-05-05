nCasos = int(input())
for i in range(nCasos):
    bonusD = 0
    bonusG = 0

    instancias = int(input())
    ataqueD, defesaD, levelD = map(int, input().split())
    if (levelD % 2 == 0):
        bonusD = instancias
    valorGolpeD = (ataqueD + defesaD) / 2 + bonusD
    ataqueG, defesaG, levelG = map(int, input().split())
    if (levelG % 2 == 0):
        bonusG = instancias
    valorGolpeG = (ataqueG + defesaG) / 2 + bonusG
    if(valorGolpeG > valorGolpeD):
        print("Guarte")
    elif(valorGolpeG==valorGolpeD):
        print("Empate")
    else:
        print("Dabriel")

