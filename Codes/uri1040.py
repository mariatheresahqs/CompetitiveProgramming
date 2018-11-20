n1, n2, n3, n4 = input().split(" ")

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = round(n1*2 + n2*3 + n3*4 + n4)/10.0

print("Media: {}".format(media))

if (media>=7.0):
    print("Aluno aprovado.")

elif (media>=5.0) and (media<6.9):
    print("Aluno em exame.")
    ne = float(input())
    print("Nota do exame: {}".format(ne))
    media = (media + ne)/2.0
    if (media>=5.0):
        print("Aluno aprovado.")
    else:
        media = round(media)
        print("Aluno reprovado.")
    print("Media final: {}".format(media))

else:
    print("Aluno reprovado.")
