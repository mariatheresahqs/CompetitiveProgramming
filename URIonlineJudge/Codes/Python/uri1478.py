n = int(input())

while n!=0:
    matriz = [[1 for i in range(n)] for j in range(n)]
    v=1
    for j in range(n):
        for i in range(j,n):
            matriz[j][i] = v 
            matriz[i][j] = v
            v+=1
        v=1
    for i in range(n):
        for j in range(n):
            if j!=n-1:
                print("{:>3}".format(matriz[i][j]),end= " ")
            else:
                print("{:>3}".format(matriz[i][j]))
    print()

    n = int(input())
