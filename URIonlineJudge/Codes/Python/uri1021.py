n = float(input())

nota100 = n//100
n = n%100
nota50 = n//50
n = n%50
nota20 = n//20
n = n%20
nota10 = n//10
n = n%10
nota5 = n//5
n = n%5
nota2 = n//2
n = n%2
moeda1 = n//1
n = n%1
moeda50 = n//0.5
n = n%0.5
moeda25 = n//0.25
n = n%0.25
moeda10 = n//0.1
n = n%0.1
moeda05 = n//0.05
n = n%0.05
moeda01 = round(n, 2)/0.01

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(nota100)))
print("{} nota(s) de R$ 50.00".format(int(nota50)))
print("{} nota(s) de R$ 20.00".format(int(nota20)))
print("{} nota(s) de R$ 10.00".format(int(nota10)))
print("{} nota(s) de R$ 5.00".format(int(nota5)))
print("{} nota(s) de R$ 2.00".format(int(nota2)))

print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(moeda1)))
print("{} moeda(s) de R$ 0.50".format(int(moeda50)))
print("{} moeda(s) de R$ 0.25".format(int(moeda25)))
print("{} moeda(s) de R$ 0.10".format(int(moeda10)))
print("{} moeda(s) de R$ 0.05".format(int(moeda05)))
print("{} moeda(s) de R$ 0.01".format(int(moeda01)))
