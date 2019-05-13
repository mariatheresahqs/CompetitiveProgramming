import math
import decimal

while True:
    try:
        valor = float(input())
        taxa = float(input())
        meses = int(input())

        # valor = decimal.Decimal(valor)
        # taxa = decimal.Decimal(taxa)
        # meses = int(meses)
        # print(valor, taxa, meses)

        simples = valor * taxa * meses
        montante = valor * pow(1 + taxa, meses)
        comp = montante - valor
        diferenca = simples - comp
        if (diferenca < 0):
            diferenca = (-1) * diferenca


        print("DIFERENCA DE VALOR = {:.2f}".format(diferenca))
        print("JUROS SIMPLES = {:.2f}".format(simples))
        print("JUROS COMPOSTO = {:.2f}".format(comp))

    except EOFError:
        break