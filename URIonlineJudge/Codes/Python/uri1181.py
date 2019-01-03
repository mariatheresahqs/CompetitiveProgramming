n = int(input())
letter = input()

aux = 0

array = [[0 for i in range(12)] for j in range(12)]

for i in range(12):
    for j in range(12):
        array[i][j] = float(input())

if letter == 'S':
    for i in range (12):
        aux+= array[n][i]
    print("{:.1f}".format(aux))
elif letter == 'M':
    for i in range(12):
        aux+=(array[n][i])
    aux = aux/12    
    print("{:.1f}".format(aux))
