positivo=0
negativo=0
par=0
impar=0

for i in range(0, 5):
    n = int(input())
    if n%2==0:
        par+=1
    if n%2!=0:
        impar+=1
    if n>0:
        positivo+=1
    if n<0:
        negativo+=1

print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(par,impar,positivo,negativo))
