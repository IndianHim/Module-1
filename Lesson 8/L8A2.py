# 1) Ask the user to enter the numerator and store it in `numn`.
numn = input(" Give me any number. ")
# 2) Ask the user to enter the denominator and store it in `numd`.
numd = input("Now give me a denominator")
# 3) Check if `numn` is divisible by `numd`:
if numn % numd == 0 : 
    print("They are divisable")
else : 
    print (" They are not divisable.")    
# - Find the remainder when `numn` is divided by `numd`.
print(numn % numd)
# - If the remainder is 0, it means perfectly divisible.

# 4) If divisible, print that `numn` is divisible by `numd`.

# 5) Otherwise, print that `numn` is not divisible by `numd`.