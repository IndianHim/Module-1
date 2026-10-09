print("====Welcome to the Grocery Store====")
item = input("What item would you like to buy today? Onions or Apples? ")
amount = int(input("How many items would you like to buy today? "))
a = 0.29
o = 0.14
if item == "Apples":
    print("The total cost will be", amount * a)
else:
    print("The total cost will be", amount * o)
print("Please pay at the next counter, Thank you.")       
