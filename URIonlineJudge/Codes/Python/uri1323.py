while True:
    valor = int(input())
    if(valor==0):
        break
    soma = 0
    i = 1
    for i in range(valor+1):
        soma = soma + (i*i)
    print(soma)
