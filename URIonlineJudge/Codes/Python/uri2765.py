frase = input()
for i in range(len(frase)):
    if(frase[i] == ","):
        print()
    else:
        print(frase[i], end="")
print()