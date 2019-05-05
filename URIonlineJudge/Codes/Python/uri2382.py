largura, altura, profundidade, raio = map(int, input().split())
volumeCaixa = largura*altura*profundidade
volumeEsfera = (3.14*4*(raio*raio*raio))/3
areaCaixa = 2*(largura+altura+profundidade)
areaEsfera = 4*3.14*(raio*raio)
dimensao = (altura/2)*(altura/2)+(largura/2)*(largura/2)
dimensao2 = (altura/2)*(altura/2)+(profundidade/2)*(profundidade/2)
if(volumeEsfera>=volumeCaixa and  raio*raio >= dimensao and raio*raio>=dimensao2):
    print("S")
else:
    print("N")


