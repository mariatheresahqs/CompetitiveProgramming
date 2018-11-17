values = input().split(" ")
a, b, c = values
maiorab = (int(a) + int(b) + abs( int(a)- int(b)))/2
maiorabc = (int(maiorab) + int(c) + abs( int(maiorab) - int(c)))/2
print("{} eh o maior".format(int(maiorabc)))
