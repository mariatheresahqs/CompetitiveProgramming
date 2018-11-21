a = [0 for x in range (10)]
for i in range (0, 10):
    a [i] = int(input())
    if (a[i]<=0):
        a[i] = 1
        
for i in range(0,10):
    print("X[{}] = {}".format(i, a[i]))
