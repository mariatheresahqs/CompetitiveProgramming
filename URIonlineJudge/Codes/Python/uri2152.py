nCasos = int(input())
for i in range(nCasos):
    hora, minuto, condicao = map(int,input().split())

    if(condicao==1):
        if (hora < 10 and minuto<10):
            print("0{}:0{} - A porta abriu!".format(hora, minuto))
        elif(hora<10):
            print("0{}:{} - A porta abriu!".format(hora, minuto))
        elif(minuto<10):
            print("{}:0{} - A porta abriu!".format(hora, minuto))
        else:
            print("{}:{} - A porta abriu!".format(hora, minuto))
    elif(condicao==0):
        if (hora < 10 and minuto<10):
            print("0{}:0{} - A porta fechou!".format(hora, minuto))
        elif(hora<10):
            print("0{}:{} - A porta fechou!".format(hora, minuto))
        elif(minuto<10):
            print("{}:0{} - A porta fechou!".format(hora, minuto))
        else:
            print("{}:{} - A porta fechou!".format(hora, minuto))