num = input()
num = [int(n) for n in num.split()]

a = num[0]
b = num[1]

if (b%a == 0) or (a%b == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
