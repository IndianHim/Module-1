try: 
    number=int(input("What would your first number be? "))
except ValueError as ex :  
    print("Exception: ", ex)  
print(number)
