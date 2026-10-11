rows = int(input("How many rows would you like on your triangle? "))
y = 1
for r in range (rows) :
   for i in range (r+1) :
      print(y , end = " ")
      y += 1
   print() 
   