contador = 1
while True:
    try:
        nValores = int(input())
        valores = list(map(float, input().split()))
        senha = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        maior = 0

        for i in range(0, len(senha)-1, 1):
            for j in range(0, len(valores)-i-1,1):
                if(valores[j] < valores[j+1]):
                    temp = valores[j]
                    valores[j] = valores[j+1]
                    valores[j+1]=temp
                    # troca posicao senha
                    temp2 = senha[j]
                    senha[j] = senha[j+1]
                    senha[j+1]=temp2


        print("Caso {}: ".format(contador), end="")
        contador+=1
        for i in range(nValores):
            print(senha[i], end="")
            if(i==(nValores-1)):
                print()

    except EOFError:
        break

