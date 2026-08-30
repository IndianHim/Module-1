hw=int(input(" How many Homeworks do you have pending? "))
while hw != 0 :
    v=input("Have you finished one of your homeworks. Yes or No? ") 
    if v == "Yes" :
        hw -= 1
    else :
        print("Please finish your homework.")
if hw == 0 :
    print("Congrats. You finished all your homework.")