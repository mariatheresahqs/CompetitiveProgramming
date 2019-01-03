p=0
j=0

for i in range(0,100):
    k = int(input())
    if k>p:
        p = k
        j = i+1
        i+=1
print("{}\n{}".format(p,j))
