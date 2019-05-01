while True:

    try:
        valores = input()
        contarAbriu = 0
        contarFechou = 0
        flag=0
        for i in range(len(valores)):
            if(valores[i]=="("):
                contarAbriu+=1
                antes =i+1
                flag = 1
            elif(valores[i]==")"):
                contarFechou+=1
                depois = i+1
                flag = 2
        if(contarAbriu==contarFechou and flag==2):
            print("correct")
        else:
            print("incorrect")

    except EOFError:
        break