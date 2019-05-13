valor1, valor2 = map(int, input().split())
for i in range(1, valor2+1, 1):
    if(i%valor1!=0):
        print("{} ".format(i), end="")
    if(i%valor1==0):
        print("{}".format(i))