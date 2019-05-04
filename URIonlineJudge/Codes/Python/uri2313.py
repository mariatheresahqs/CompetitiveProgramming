valor1, valor2, valor3 = map(int, input().split())
maior = 0
if(valor1<valor2+valor3 and valor2<valor3+valor1 and valor3<valor2+valor1):
    if(valor1==valor2 and valor2==valor3):
        print("Valido-Equilatero")
    elif(valor1==valor2 or valor1==valor3 or valor2==valor3):
        print("Valido-Isoceles")
    else:
        print("Valido-Escaleno")
    if((valor1*valor1 + valor2*valor2)==(valor3*valor3) or (valor3*valor3 + valor2*valor2)==(valor1*valor1) or (valor1*valor1 + valor3*valor3)==(valor2*valor2)):
        print("Retangulo: S")
    else:
        print("Retangulo: N")
else:
    print("Invalido")