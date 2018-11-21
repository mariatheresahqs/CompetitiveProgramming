num = input()
num = [float(n) for n in num.split()]

num = sorted(num, reverse=True)

a = num[0]
b = num[1]
c = num[2]

if (a>=b+c):
    print("NAO FORMA TRIANGULO")
elif (pow(a,2) == pow(b,2)+pow(c,2)):
    print("TRIANGULO RETANGULO")
elif (pow(a,2)>pow(b,2)+pow(c,2)):
    print("TRIANGULO OBTUSANGULO")
elif (pow(a,2)<pow(b,2)+pow(c,2)):
    print("TRIANGULO ACUTANGULO")
if (a==b==c):
    print("TRIANGULO EQUILATERO")
if (a==b!=c) or (a==c!=b) or (b==c!=a):
    print("TRIANGULO ISOSCELES")
