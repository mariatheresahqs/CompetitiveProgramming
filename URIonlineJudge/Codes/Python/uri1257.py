nCasos = int(input())
for i in range(nCasos):
    Casos = int(input())
    total = 0
    for j in range(Casos):
        string = input()
        indice = 0
        soma = 0
        for k in string:
            valor = (ord(k) - 65) + indice + j
            soma += valor
            # valor += valor
            # print(ord(k))
            # print(indice)
            # print(j)
            # print(soma)
            # print(valor)
            indice+=1
        total = total + soma
        # print(total)
    print(total)