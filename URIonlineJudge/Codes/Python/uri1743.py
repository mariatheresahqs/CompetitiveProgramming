vetor1 = [int(i) for i in input().split()]
vetor2 = [int(j) for j in input().split()]
flag = 1
for i in range(len(vetor1)):
    if(vetor1[i]==vetor2[i]):
        print("N")
        flag = 0
        break
if(flag==1):
    print("Y")