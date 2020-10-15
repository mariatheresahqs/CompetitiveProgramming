num = int(input())

vetorpar = []
vetorimpar = []

for i in range(num):
    num2 = int(input())
    if(num2 % 2 == 0):
        vetorpar.append(num2)
    else:
        vetorimpar.append(num2)

vetorpar =  sorted(vetorpar, key=int)
vetorimpar = sorted(vetorimpar,key=int, reverse=True)

vetor = vetorpar
vetor.extend(vetorimpar)
count = len(vetor)

for i in range(count):
    print(vetor[i])
