days = int(input())
vyear = days//365
days = days%365
vmonths = days//30
days = days%30
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(vyear, vmonths, days))
