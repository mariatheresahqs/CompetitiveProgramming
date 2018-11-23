count=0
totalpositivos=0

for n in range (0,6):
    num = float(input())
    if num>0:
        totalpositivos+=num
        count+=1
media = totalpositivos/count
        
print("{} valores positivos\n{:.1f}".format(count,media))
