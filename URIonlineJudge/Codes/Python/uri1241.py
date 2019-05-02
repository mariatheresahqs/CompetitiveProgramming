nCasos = int(input())
for i in range(nCasos):
    valor1, valor2 = input().split()
    if(len(valor1)<len(valor2)):
        print("nao encaixa")

    else:
        k = len(valor1)
        j = len(valor2)
        diferenca = k - j
        contador = 0
        indiceValor2 = 0
        for n in range(diferenca, len(valor1), 1):
            # print(valor1[n], valor2[indiceValor2])
            if(valor1[n]==valor2[indiceValor2]):
                contador+=1
                indiceValor2+=1

        if(contador==len(valor2)):
            print("encaixa")
        else:
            print("nao encaixa")

