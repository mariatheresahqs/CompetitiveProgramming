n = int(input())
csum=0
rsum=0
ssum=0

for i in range(0,n):
    t = input().split(" ")
    num = int(t[0])
    ani = t[1]
    if ani=="C":
        csum+=num
    elif ani=="R":
        rsum+=num
    elif ani=="S":
        ssum+=num
total = ssum + rsum + csum
pc = (csum*100)/total
pr = (rsum*100)/total
ps = (ssum*100)/total
print("Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}\nPercentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %".format(total,csum,rsum,ssum,pc,pr,ps))
