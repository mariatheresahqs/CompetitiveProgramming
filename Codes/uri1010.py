line1 = input().split(" ")
line2 = input().split(" ")
code1, qtd1, value1 = line1
code2, qtd2, value2 = line2
print("VALOR A PAGAR: R$ %.2f" %(int(qtd1) * float(value1) + int(qtd2) * float(value2)))
