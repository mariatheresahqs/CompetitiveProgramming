line1 = input().split(" ")
line2 = input().split(" ")
x1, y1 = line1
x2, y2 = line2
distance = ((float(x2) - float(x1))**2) + ((float(y2) - float(y1))**2)
dsqrt = distance**(1/2)
print("{:.4f}".format(dsqrt))
