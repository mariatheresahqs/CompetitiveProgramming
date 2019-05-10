while True:
    try:
        a,b,c,d= map(int, input().split())
        if a==b==c==d==0:
            break
        altura = (c*((a/2)+b))/d
        print("{:.5f}".format(altura))
    except EOFError:
        break