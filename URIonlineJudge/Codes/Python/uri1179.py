even = []
odd = []

countodd = 0
counteven = 0
count = 0

while count!=15:
    n = int(input())
    if n%2==0:
        even.append(n)
        counteven+=1
    else:
        odd.append(n)
        countodd+=1
    if counteven==5:
        for i in range(5):
            print("par[{}] = {}".format(i,even[i]))
        counteven = 0
        even.clear()
    if countodd==5:
        for i in range(5):
            print("impar[{}] = {}".format(i,odd[i]))
        countodd = 0
        odd.clear()
    count+=1
for i in range(len(odd)):
    print("impar[{}] = {}".format(i,odd[i]))
for i in range(len(even)):
    print("par[{}] = {}".format(i, even[i]))
