import math
a, b, c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)

bsk = (pow(b, 2) - 4*a*c)

if ( bsk < 0) or (a ==0):
    print("Impossivel calcular")

else:
    r2 = (-b - math.sqrt(bsk))/(2*a)
    r1 = (-b + math.sqrt(bsk))/(2*a)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(r1, r2))