letter = input()

tam = 12
aux = 0
count = 0

array = [[0 for i in range(tam)]for j in range(tam)]

for i in range(tam):
    for j in range(tam):
        array[i][j] = float(input())
        
for i in range(tam):
    for j in range(tam):
        if j>i:
            aux+=array[i][j]
            count+=1
            
if letter == 'S':
    print("{:.1f}".format(aux))  

elif letter == 'M':
    print("{:.1f}".format(aux/count))
