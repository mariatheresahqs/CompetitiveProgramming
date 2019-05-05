nValores = int(input())
valores = [int(i) for i in input().split()]
flag = 0
for k in range(nValores-1):
    if(valores[k]>valores[k+1]):
        print(k+2)
        flag = 1
        break
if(flag==0):
    print("0")
