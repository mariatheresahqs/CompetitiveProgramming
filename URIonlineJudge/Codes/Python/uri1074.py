k = int(input())

for i in range(0,k):
    n = int(input())
    if n>0:
        if n%2==0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif n<0:
        if n%2==0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    else:
        print("NULL")
        
    i+=1
