nJogadores = int(input())
stotal = btotal = atotal = Sstotal = Sbtotal = Satotal = 0
for i in range(nJogadores):
    nome = input()
    saques, bloqueios, ataques = map(int,input().split())
    Ssaque, Sbloqueio, Sataque = map(int,input().split())
    stotal+= saques
    btotal+= bloqueios
    atotal+=ataques
    Satotal+=Sataque
    Sbtotal+=Sbloqueio
    Sstotal+=Ssaque
print("Pontos de Saque: {:.2f} %.".format(100*Sstotal/float(stotal)))
print("Pontos de Bloqueio: {:.2f} %.".format(100*Sbtotal/float(btotal)))
print("Pontos de Ataque: {:.2f} %.".format(100*Satotal/float(atotal)))