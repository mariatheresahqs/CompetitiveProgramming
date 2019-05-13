valor1, valor2 = map(int, input().split())
soma = ((valor1+valor2)*(valor2-valor1+1))/2
print("{:.0f}".format(soma))