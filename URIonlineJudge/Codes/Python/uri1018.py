a=int(input())
print(a)
v100=a//100
a= a%100
v50=a//50
a=a%50
v20=a//20
a=a%20
v10=a//10
a=a%10
v5=a//5
a=a%5
v2=a//2
a=a%2
v1=a//1
print('{} nota(s) de R$ 100,00'.format(v100))
print('{} nota(s) de R$ 50,00'.format(v50))
print('{} nota(s) de R$ 20,00'.format(v20))
print('{} nota(s) de R$ 10,00'.format(v10))
print('{} nota(s) de R$ 5,00'.format(v5))
print('{} nota(s) de R$ 2,00'.format(v2))
print('{} nota(s) de R$ 1,00'.format(v1))
