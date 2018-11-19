values = input().split(" ")
a, b, c = values

tri= (float(a) * float(c))/2
circle= 3.14159 * (float(c) * float(c))
trap= float(c) * (float(a) + float(b))/2
square= float(b) * float(b)
rect= float(a) * float(b)

print("TRIANGULO: {:.3f}".format(tri))
print("CIRCULO: {:.3f}".format(circle))
print("TRAPEZIO: {:.3f}".format(trap))
print("QUADRADO: {:.3f}".format(square))
print("RETANGULO: {:.3f}".format(rect))
