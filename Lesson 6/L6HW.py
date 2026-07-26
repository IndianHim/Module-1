print("====Library Visit====")
print("I will plan your library visit with 3 questions")
day = input("What day of the week is it? ")
weather = input("What is the weather like today? Sunny, Cloudy, or Raining. ")
book = input("Do you have a book that is due? " )
if day == "Monday" or weather == "Sunny" or weather == "Cloudy" and book == "Yes" :
    print ("It sounds like today would be a great day to go to the library! ")
elif day == "Tuesday" or day == "Wednesday" or day == "Thursday" or weather == "Raining" and book == "Yes" :
    print("Today does not seem like the right day to go to the library to return that book.")
elif day == "Friday" or weather == "Sunny" or weather == "Cloudy" or book == "Yes" :
    print("It sounds like today would be a great day to go to the library! ")  
elif book == "No" :
   print("If you do not have a book to return, then you should not go to the library at all then.")    