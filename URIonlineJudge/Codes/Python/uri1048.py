salary = float(input())

if salary>0 and salary<=400:
    salaryf = salary*1.15
    reajuste = salaryf-salary
    percent = 15
elif salary>400 and salary<=800:
    salaryf = salary*1.12
    reajuste = salaryf-salary
    percent = 12
elif salary>800 and salary<=1200:
    salaryf = salary*1.10
    reajuste = salaryf-salary
    percent = 10
elif salary>1200 and salary<=2000:
    salaryf = salary*1.07
    reajuste = salaryf-salary
    percent = 7
elif salary>2000:
    salaryf = salary*1.04
    reajuste = salaryf-salary
    percent = 4
print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %".format(salaryf,reajuste,percent))
