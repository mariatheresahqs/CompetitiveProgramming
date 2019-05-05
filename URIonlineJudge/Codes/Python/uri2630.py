nCasos = int(input())
for i in range(nCasos):
    comando = input()
    rgb = list(map(int,input().split()))
    resultado =0
    if(comando == "min"):
        menor = rgb[0]
        if(rgb[1]<menor):
            resultado = rgb[1]
        elif(rgb[2]<menor):
            resultado = rgb[2]
    elif(comando == "max"):
        maior = rgb[0]
        if (rgb[1] > maior):
            resultado = rgb[1]
        elif (rgb[2] > maior):
            resultado = rgb[2]
    elif(comando=="mean"):
        resultado = (rgb[0] + rgb[1] + rgb[2])//3
    elif(comando == "eye"):
        resultado = int(0.30*rgb[0] + 0.59*rgb[1] + 0.11*rgb[2])
    print("Caso #{}: {}".format(i + 1, int(resultado)))

