time = input()
time = [int(n) for n in time.split()]

timestart = time[0]
timeend = time[1]

if timeend>timestart:
    n = timeend-timestart
    
else:
    n = (23-timestart)+(timeend+1)
    
print("O JOGO DUROU {} HORA(S)".format(n))
