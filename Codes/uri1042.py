num = input()
num = [int(n) for n in num.split(" ")]

n1 = num[0]
n2 = num[1]
n3 = num[2]

num = sorted(num)

print("{}\n{}\n{}\n".format(num[0], num[1], num[2]))
print("{}\n{}\n{}".format(n1, n2, n3))
