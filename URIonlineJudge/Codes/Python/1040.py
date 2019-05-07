n1, n2, n3, n4 = input().split(" ")

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1*2 + n2*3 + n3*4 + n4*1)/10

print("Media: {}".format(media)

if (media>= 7.0)
    print("Aluno aprovado")
elif (media<5.0):
    print("Aluno reprovado")
else:
    print("Aluno em exame")
    ne = float(input())
    media = (media + ne)/2
    print("Nota do exame: {}".format(ne))
    if (media>=5.0):
        print("Aluno aprovado")
    elif (media<5.0):
        print("Aluno reprovado")
    print("Media final: {}".format(media))
