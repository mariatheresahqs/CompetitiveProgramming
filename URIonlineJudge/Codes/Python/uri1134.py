product = int(input())
alcohol = 0
gasoline = 0
diesel = 0
x=1
while (x==1):
    product = int(input())
    if (product==1):
        alcohol+=1
    elif (product==2):
        gasoline+=1
    elif (product==3):
        diesel+=1
    elif (product==4):
        break

print("MUITO OBRIGADO")
print("Alcool: {}".format(alcohol))
print("Gasolina: {}".format(gasoline))
print("Diesel: {}".format(diesel))
