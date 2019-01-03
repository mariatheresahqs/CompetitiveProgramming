n = int(input())
i=0
countin=0
countout=0

while i<n:
    x = int(input())
    i+=1
    if x>=10 and x<=20:
        countin+=1
    else:
        countout+=1
print("{} in\n{} out".format(countin,countout))
