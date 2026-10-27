bill = int(input("What was the price of your meal? ")) 
tip  = int(input("What will the tip percantage be that you will be donating today? "))
def total_calc(bill,tip):
    total =  (bill + bill * (tip / 100))
    return total
print(total_calc(bill,tip))
