time = input()
time = [int(i) for i in time.split(" ")]

hours = time[0]
mins = time[1]
houre = time[2]
mine = time[3]

if houre>hours:
    hour = houre - hours
elif hours>houre:
    hour = (24-hours)+(houre)
elif hours==houre and mine>mins:
    hour = 0
    minu = mine - mins
elif hours==houre:
    hour = 24
if mine>=mins:
    minu = mine - mins
elif mins>mine:
    minu = (60-mins)+(mine)
    hour-=1
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hour,minu))
