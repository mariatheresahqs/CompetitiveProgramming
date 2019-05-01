nCasos = int(input())

for i in range(nCasos):
    frase = input()
    tamanho = len(frase)
    metade = tamanho//2
    for i in range((metade-1), -1, -1):
        print(frase[i], end='')
    for i in range(tamanho-1, metade-1,-1):
        print(frase[i], end='')
    print()