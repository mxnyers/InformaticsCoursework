#Question 1
user_height = 45

if user_height > 70:
    print("true")
else:
    print("false")

#Question 2
name = "Nora"

if name == "" or name == "test":
    print("true")
else:
    print("false")

#Question 3
country = "USA"
currency = "dollar"

if country == "USA" and currency == "dollar":
    print("true")
else:
    print("false")

#Question 3, Version 2
country = input("Please enter a country: ")
currency = input("Please enter a currency: ")

if country == "USA" and currency == "dollar":
    print("true")
else:
    print("false")

#Question 4
print("What would you like to do this weekend?")
answer = input("Do you want to go to the park or a movie? ")

if answer == "park" or answer == "movie":
    if answer == "park":
        print("Great! Let's go!")
    else:
        movie_answer = input("Is it true that we have enough money for tickets? [True, False] ")
        if movie_answer == "True":
            print("Excellent! Bring on the popcorn.")
        else:
            print("That's okay. It's a nice day for the park.")
else:
    print("That's not something we can do this weekend.")

#Question 5
def questionFive():
    #Putting entire code into function so user won't have to restart incase of USER error

    number_list = eval(input("Please enter a list of numbers (x, y, z, etc.]: "))
    number_list.sort()

    print("The largest number in your list is: ", number_list[-1])
    print("The smallest number in your list is: ", number_list[0])

    choice = input("Would you like to Add or Remove one? ")

    if choice == "Add" or choice == "Remove":
        if choice == "Add":
            number_list.append(eval(input("What is the new number? ")))
            print(number_list)
        else:
            remove = eval(input("What number should we remove? "))
            if remove in number_list:
                number_list.remove(remove)
                print(number_list)
            else:
                print("That number isn't in the list!")
                questionFive() #Resarting the function because of the user error
    else:
        print("That is not a valid choice!")
        questionFive() #Restarting the function because of the user error

questionFive() #Calling the function, IMPORTANT because otherwise it won't work
