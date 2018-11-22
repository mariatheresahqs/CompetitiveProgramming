salary = float(input())

t8 = (salary-2000.00)*0.08
t18 = (salary-3000.00)*0.18 + (1000.00)*0.08
t28 = (salary-4500.00)*0.28 + (1500.00)*0.18 + (1000.00)*0.08

if salary<=2000.00:
    print("Isento")
elif salary>2000.00 and salary<=3000.00:
    print("R$ {:.2f}".format(t8))
elif salary>3000.00 and salary<=4500.00:
    print("R$ {:.2f}".format(t18))
elif salary>4500.00:
    print("R$ {:.2f}".format(t28))
