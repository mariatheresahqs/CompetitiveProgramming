names1 = input()
names2 = input()
names3 = input()

if names1=="vertebrado":
    if names2=="ave":
        if names3=="carnivoro":
            print("aguia")
        elif names3=="onivoro":
            print("pomba")
    elif names2=="mamifero":
        if names3=="onivoro":
            print("homem")
        elif names3=="herbivoro":
            print("vaca")
elif names1=="invertebrado":
    if names2=="inseto":
        if names3=="hematofago":
            print("pulga")
        elif names3=="herbivoro":
            print("lagarta")
    elif names2=="anelideo":
        if names3=="hematofago":
            print("sanguessuga")
        elif names3=="onivoro":
            print("minhoca")
