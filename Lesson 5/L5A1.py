#A Weather Outfit Picker that asks about temperature, rain, wind, and puddles, 
# then uses if and if-else statements to decide what outfit, umbrella, windbreaker, 
# and shoes to wear, all while keeping every block properly indented.
weather = input("What is the weather like today? ")
Wind = int(input("How windy is it today out of ten? "))
Rain = input("Has it rained in the past few days? ").lowercase()
if weather == "hot" :
    print("You could wear shorts and a t-shirt today.")
elif weather == "cold" :
    print("You could wear sweatpants with a hoodie.")
else :
    print("You could wear shorts, a t-shirt, and a hoodie.")
if 1 <= Wind <= 4 :
    print("You could wear shorts and a t-shirt today.") 
elif 5 <= Wind <= 7 :
    print("You could wear shorts, a t-shirt, and a hoodie.")    
elif 8 <= Wind <= 10 :
    print("You could wear sweatpants with a hoodie.")    
if Rain == "yes" :
    print("Today you might want to wear some rain boots")
else :
    print("You are free to wear whatever shoes you would like. =)")    


