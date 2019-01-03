fib = [0 for x in range (61)]
fib[0] = 0
fib[1] = 1

for i in range (2, 61):
    
    fib[i]= fib[i-1]+fib[i-2]
t = int(input())

n = [0 for x in range (t)]

for i in range (0, t):
    n[i] = int(input())
    
for i in range (0, t):
    print("Fib({}) = {}".format(n[i], fib[n[i]] ))
