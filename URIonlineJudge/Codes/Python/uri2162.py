nValores = int(input())
valores = list(map(int,input().split()))
flag = 1
if(nValores==2 and valores[0]==valores[1]):
    flag = 0
else:
    for i in range(2, nValores, 1):
        if(valores[i] >= valores[i-1] and valores[i-1] >= valores[i-2]):
            flag = 0
            break
        elif(valores[i] <= valores[i-1] and valores[i-1] <= valores[i-2]):
            flag = 0
            break
print(flag)