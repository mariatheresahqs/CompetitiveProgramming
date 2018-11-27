n = int(input())
letter = input()

tam = 12
soma = 0
media = 0

array = [[0 for i in range(tam)] for j in range(tam)]

for i in range(tam):
    for j in range(tam):
        array[i][j] = float(input())
        
if letter == 'S':
    for j in range(tam):
        soma+=array[j][n]
    print("{:.1f}".format(soma))
        
elif letter == 'M':
    for j in range(tam):
        soma+=array[j][n]
    media = soma/tam
    print("{:.1f}".format(media))
