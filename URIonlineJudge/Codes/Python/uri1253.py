nCasos = int(input())

for i in range(nCasos):
    palavra = input()
    deslocamento = int(input())
    novaPalavra = ''
    for l in palavra:
        posicao = ord(l)-deslocamento

        if(posicao < 65):
            novaPalavra += chr(91-(65-posicao))
        else:
            novaPalavra += chr(posicao)
    print(novaPalavra)