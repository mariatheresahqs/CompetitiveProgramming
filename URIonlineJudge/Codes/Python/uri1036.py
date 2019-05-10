import math
nCasos = int(input())
for i in range(nCasos):
    a, b, c = map(int, input().split())
    bsk = (b*b - 4*a*c)

    r1 = (-b - math.sqrt(bsk))/(2*a)
    r2 = (-b + math.sqrt(bsk))/(2*a)

    xMedio = (r1+r2)/2
    altura = xMedio*xMedio*a + xMedio*b + c

    print("{:.2f}".format(altura))