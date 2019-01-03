time=int(input())
min=time//60
time=time%60
hour=min//60
min=min%60
print('{}:{}:{}'.format(hour,min,time))
