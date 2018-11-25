n = int(input())

for i in range(0,n):
    tc = input()
    tc = [float(x) for x in tc.split()]
    avg = (tc[0]*2 + tc[1]*3 + tc[2]*5)/10
    i+=1
    print("{:.1f}".format(avg))
