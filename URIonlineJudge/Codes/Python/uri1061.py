days = input().split(" ")
days = int(days[1])

times = input().split(" ")
hours = int(times[0])
minus = int(times[2])
secs = int(times[4])

daye = input().split(" ")
daye = int(daye[1])

timee = input().split(" ")
houre = int(timee[0])
minue = int(timee[2])
sece = int(timee[4])

dayd = daye - days
hourd = houre - hours
mind = minue - minus
secd = sece - secs

if hours>houre:
    dayd-=1
    hourd = (24 - hours) + houre
        
if minus>minue:
        hourd-=1
        mind = (60 - minus) + minue
        
elif minus==minue and secs>sece:
        hourd-=1
        mind = (60 - minus) + minue

if secs>sece:
        mind-=1
        secd = (60 - secs) + sece

print("{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)".format(dayd, hourd, mind, secd))
