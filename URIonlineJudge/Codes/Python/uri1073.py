a = int(input())
for n in range(1,(a+1)):
    if (n%2==0):
        k = pow(n,2)
        print("{}^2 = {}".format(n, k))
