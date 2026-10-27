#Adding Art Supplies Homeworkk
def greeting ():
    print(" =====Welcome to the Art Supplies Store=====")
    print(" Here is where you can purchase all your needed Art Supplies.")
    print(" What would you like to purchase today?")
greeting()
colors = 1.5
brushes = 2.5
constructionpaper = 3.5
def items ():
    print(" We have the variety of colors, brushes, and construction paper. What would you like today?")
    c  = int(input("    How many colors would you like today? "))
    b  = int(input("    How many brushes would you like today? "))
    cp = int(input("    How many construction papers would you like today? "))
    return c,b,cp
def price (c,b,cp) :
 Total = float((c * colors) + (b * brushes) + (cp * constructionpaper))
 print (    Total,"dollars will be your total today.")
c,b,cp = items ()
price (c,b,cp)
def payment ():
   input("  Will that be Cash or Card today? ")
   print ("  Cha Ching")
   print("  Thank you for shopping at the Art Supplies Store today. Come Again ! ")
payment()
