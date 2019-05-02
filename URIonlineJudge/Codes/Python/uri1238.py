nCasos = int(input())

for i in range(nCasos):
    palavra = []
    cadeia1, cadeia2 = map(str, input().split())
    maior = len(cadeia1)
    if(maior<len(cadeia2)):
        maior = len(cadeia2)
    for i in range(maior):
        if(i<len(cadeia1)):
            print(cadeia1[i], end='')
        if(i<len(cadeia2)):
            print(cadeia2[i], end='')
    print()