n = int(input())
vector = [0 for i in range(n)]
v = input().split(" ")
for i in range(n):
    vector[i] = int(v[i])

smallest = vector[0]
position = 0
for i in range(1,n):
    if vector[i] < smallest:
        smallest = vector[i]
        position = i
print("Menor valor: {}".format(smallest))
print("Posicao: {}".format(position))
