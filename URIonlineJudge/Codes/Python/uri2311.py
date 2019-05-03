nCompetidores = int(input())
nota = []
for i in range(nCompetidores):
    nome = input()
    dificuldade = float(input())
    resultado = 0.0
    # nota = [0 for x in range(7)]
    nota = list(map(float, input().split()))
    maior = nota[0]
    menor = nota[0]
    for i in range(7):
        resultado+= nota[i]
        if(nota[i]>maior):
            maior = nota[i]
        if(nota[i]<menor):
            menor = nota[i]
    resultado = (resultado - menor - maior)*dificuldade

    print("{} {:.2f}".format(nome, resultado))
