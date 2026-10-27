import array
int_array = []
num=int(input("How many numbers would you like to input today? Please enter a number 10 or under. "))
while num > 10 :
    print("Your response is a invalid one. Please now enter a valid response.")
    num=int(input("How many numbers would you like to input today? Please enter a number 10 or under. "))
for i in range (num):
    user_input = int(input(f"Enter your input: {i + 1} of 10. "))
    int_array.append(user_input)
 #   int_array.sort()
print("Your integer array:", int_array)
for i in range(num,1):
    smallest = int_array[i-1]
    print ("i = ", i , "smallest = ", smallest )
    for j in (num, i):
        if smallest > int_array[j]:
            smallest_position = j
            smallest = int_array[j]
            print ("j = ", j , "smallest = ", smallest )
    temp = int_array [i-1]
    int_array [i-1] = smallest
    int_array [smallest_position] = temp
print ("Sorted array : ",int_array,)





    