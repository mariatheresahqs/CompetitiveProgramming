import math
cont = 0
time = int(input())
for i in range(0,time):
    var = input().split(" ")
    PA = float(var[0])
    PB = float(var[1])
    G1 = float(var[2])
    G2 = float(var[3])
    while (PA<=PB):
        PA = math.floor(PA + PA*(G1/100))
        PB = math.floor(PB + PB*(G2/100))
        cont+= 1
        if (cont>100):
            break
    if (cont<=100):
        print ("{} anos.".format(cont))
    else:
        print ("Mais de 1 seculo.")
    cont = 0
