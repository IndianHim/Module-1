# 1) Store values in `v`, `w`, `x`, `y`, and `z`.
v= 5
w = 4
x = 6
y = 3
z = 10
# 2) Calculate the expression (v + w) * x / y and store the result back in `z`.
z = (v + w) * x / y
# 3) Print the value of `z` with a message.
print (z, "If the first number you see is 18 then this code is running correctly.")
# 4) Store a name in `name` and a number in `age`.
name = "Ryan"
age = 13
# 5) Check this condition using `or` and `and`:
if name == "Alex" and age == 13 :
    print(" Uh Oh")
elif name == "Alex" or age == 13  :
    print("The name is not Alex.")    
# - The code checks if `name` is "Alex"

# OR (if `name` is "John" AND `age` is 2 or more).
if name == "John" and age >= 2 :
    print("Cool!")
# - If the condition is true, print the welcome message.
if name == "Ryan" and age <= 13 :
    print ("Very Nice!")
else : 
    print("GoodBye")    
# - Otherwise, print the goodbye message.
