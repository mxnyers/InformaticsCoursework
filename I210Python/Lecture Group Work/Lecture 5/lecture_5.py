###Temperature Conversion Algorithm
##temp = eval(input("Please enter a temperature: "))
##
##fahrenheit = (temp * (9/5)) + 32
##celcius = (temp - 32) * (5/9)
##
##user_input = input("Would you like that converted to C or F? ")
##
##if user_input == "C":
##    print(temp," F is ", celcius, " C.")
##elif user_input == "F":
##    print(temp," C is ", fahrenheit, " F.")
##else:
##    print("You didn't enter C or F!")

user_input = eval(input("Please enter any number: "))

if user_input % 2  == 0:
    print("Even number detected!")

elif user_input % 2 == 1:
    print("Odd number detected!")

else:
    print("Float detected!")
    
