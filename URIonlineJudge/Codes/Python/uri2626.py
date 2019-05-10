while True:
    try:

        dodo, leo, peper = input().split()
        vencedor = 0
        if(dodo==leo and leo==peper):
            vencedor = 4
        elif(dodo!=leo and leo!=peper and peper!=dodo):
            vencedor = 4

        elif (dodo == "papel"):
            if (leo == peper == "pedra"):
                vencedor = 1
            elif (dodo == peper or dodo == leo):
                vencedor = 4
            if(leo=="tesoura"):
                vencedor = 2
            if(peper=="tesoura"):
                vencedor = 3
            if(leo==peper=="tesoura"):
                vencedor = 4


        elif (dodo == "pedra"):
            if (leo == peper == "tesoura"):
                vencedor = 1
            elif (dodo == peper or dodo == leo):
                vencedor = 4
            if(leo=="papel"):
                vencedor = 2
            if(peper=="papel"):
                vencedor = 3
            if (leo == peper == "papel"):
                vencedor = 4


        elif (dodo == "tesoura"):
            if (leo == peper == "papel"):
                vencedor = 1
            elif (dodo == peper or dodo == leo):
                vencedor = 4
            if(leo=="pedra"):
                vencedor = 2
            if(peper=="pedra"):
                vencedor = 3
            if (leo == peper == "pedra"):
                vencedor = 4


        if(vencedor==1):
            print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
        elif(vencedor==2):
            print("Iron Maiden's gonna get you, no matter how far!")
        elif(vencedor==3):
            print("Urano perdeu algo muito precioso...")
        elif(vencedor==4):
            print("Putz vei, o Leo ta demorando muito pra jogar...")


    except EOFError:
        break