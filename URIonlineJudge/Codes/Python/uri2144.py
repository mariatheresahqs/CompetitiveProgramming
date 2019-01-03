medias = 1
for i in range(1, 10000):
    W = input().split(" ")
    W1 = int(W[0]) 
    W2 = int(W[1])
    R = int(W[2])
    M = float(W1 + W2)/2*(1 + int(R)/30)
    if W1==0 and W2==0 and R==0:
        break
    if 1 <=W1<= 60:
        if 1 <=W2<= 100:
            if (1<=M<13):
                print("Nao vai da nao")
            elif (13<=M<14):
                print("E 13")
            elif (14<=M<40):
                print("Bora, hora do show! BIIR!")
            elif (40<=M<=60):
                print("Ta saindo da jaula o monstro!")
            elif (M>60):
                print("AQUI E BODYBUILDER!!")
            medias = medias + M
if medias > 40:
 print("\nAqui nois constroi fibra rapaz! Nao e agua com musculo!")
