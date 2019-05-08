while True:

    hours, mins, houre, mine = map(int, input().split())

    if(hours ==0 and mins==0 and houre==0 and mine==0):
        break

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

    tempoTotal = (hour*60) + minu
    print(tempoTotal)