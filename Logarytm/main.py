import logarytm

try:
    l1 = logarytm.Logarytm(2,4)
    l2 = logarytm.Logarytm(2,8)
    l3 = logarytm.Logarytm(7,5)
    # l4 = logarytm.Logarytm(1,9)
    # l5 = logarytm.Logarytm(2,1)

    print ("l1= ", l1)
    print("l2= ", l2)
    print("l3= ", l3)

    print("l1 + l2 = ", l1+l2)
    print("l2 + l3 = ", l2+l3)

    print(l1," => ",l1.oblicz())



except logarytm.ZlaPodstawa as zp:
    print (zp)
except logarytm.ZlyArgument as za:
    print (za)
except logarytm.RoznePodstawy as rp:
    print (rp)