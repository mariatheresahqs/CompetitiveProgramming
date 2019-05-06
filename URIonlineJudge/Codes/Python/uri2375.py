diametro = int(input())
volumeEsfera = (4*3.14*(diametro/2))/3
altura, largura, profundidade = map(int, input().split())
volumeCaixa = altura*largura*profundidade
if(volumeCaixa>=volumeEsfera and diametro<=altura and diametro<=profundidade and diametro<=largura):
    print("S")
else:
    print("N")