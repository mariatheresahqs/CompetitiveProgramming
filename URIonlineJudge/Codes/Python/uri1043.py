num = input()
num = [float(n) for n in num.split()]

a = num[0]
b = num[1]
c = num[2]

if ((a + b)>c) and ((a+c)>b) and ((b+c)>a):
    print("Perimetro = {}".format(a+b+c))

else:
    print("Area = {}".format(c*(a+b)/2))
