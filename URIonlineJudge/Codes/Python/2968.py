import math

entrada = input().split(" ")

total = int(entrada[0]) * int(entrada[1])

dez = math.ceil(10*total/100)
vinte = math.ceil(20*total/100)
trinta = math.ceil(30*total/100)
quarenta = math.ceil(40*total/100)
cinquenta = math.ceil(50*total/100)
sessenta = math.ceil(60*total/100)
setenta = math.ceil(70*total/100)
oitenta = math.ceil(80*total/100)
noventa = math.ceil(90*total/100)

print(dez,vinte,trinta,quarenta,cinquenta,sessenta, setenta,oitenta,noventa)
