contador = 0
sorteado = 0
while (contador<3):
    sinal = input()
    if(sinal == "---"):
        sorteado += 0
    elif(sinal == "--*"):
        sorteado+=1
    elif(sinal == "-*-"):
        sorteado+=2
    elif (sinal == "-**"):
        sorteado += 3
    elif(sinal == "*--"):
        sorteado+=4
    elif(sinal == "*-*"):
        sorteado+=5
    elif(sinal =="**-"):
        sorteado+=6
    elif (sinal == "***"):
        sorteado += 7
    elif(sinal == "caw caw"):
        print(sorteado)
        sorteado = 0
        contador+=1