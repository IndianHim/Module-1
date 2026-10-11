b = int(input("What number would you like for the base in your exponential equation?  "))
e = int(input("What number would you like for your exponent? "))
for i in range (e-1) :
    b = b * b
print (b)