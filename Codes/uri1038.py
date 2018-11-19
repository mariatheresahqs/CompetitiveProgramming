product = input().split(" ")
productcode = int(product[0])
quantity = int(product[1])
if (productcode == 1):
    print ("Total: R$ %.2f"%(4*quantity))
elif (productcode == 2):
    print ("Total: R$ %.2f"%(4.5*quantity))
elif (productcode == 3):
    print ("Total: R$ %.2f"%(5*quantity))
elif (productcode == 4):
    print ("Total: R$ %.2f"%(2*quantity))
elif (productcode == 5):
    print ("Total: R$ %.2f"%(1.5*quantity))
