while True:
    try:
        contador = 0
        qnt = int(input())
        if(qnt==1):
            print(0)
        else:
            while(qnt>1):
                contador+=1
                qnt = qnt/2
            print(contador)
    except EOFError:
        break