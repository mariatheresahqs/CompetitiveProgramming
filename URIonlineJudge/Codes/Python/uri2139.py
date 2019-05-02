while True:
    try:
        mes, dia = map(int, input().split())
        if(mes==12 and dia==25):
            print("E natal!")
        elif(mes==12 and dia==24):
            print("E vespera de natal!")
        elif(mes==12 and dia>25):
            print("Ja passou!")
        else:
            um = 31
            dois = 29
            tres = 31
            quatro = 30
            cinco = 31
            seis = 30
            sete = 31
            oito = 31
            nove = 30
            dez = 31
            onze = 30
            if(mes==12):
                faltam = 24 - dia
            elif(mes==11):
                faltam = (30-dia) + 25
            elif(mes==10):
                faltam = 25 + onze + (31 - dia)
            elif(mes==9):
                faltam = 25 + dez + onze + (30-dia)
            elif(mes==8):
                faltam = 25 + nove + dez + onze + (31-dia)
            elif(mes==7):
                faltam = 25 + oito + nove + dez + onze + (31 - dia)
            elif(mes == 6):
                faltam = 25 + sete + oito + nove + dez + onze + (30 - dia)
            elif(mes == 5):
                faltam = 25 + seis + sete + oito + nove + dez + onze + (31 - dia)
            elif(mes == 4):
                faltam = 25 + cinco + seis + sete + oito + nove + dez + onze + (30 - dia)
            elif(mes == 3):
                faltam = 25 + quatro + cinco + seis + sete + oito + nove + dez + onze + (31 - dia)
            elif(mes == 2):
                faltam = 25 + tres + quatro + cinco + seis + sete + oito + nove + dez + onze + (29 - dia)
            elif(mes == 1):
                faltam = 25 + dois + tres + quatro + cinco + seis + sete + oito + nove + dez + onze + (31 - dia)

            print("Faltam {} dias para o natal!".format(faltam))

    except EOFError:
        break
