######################
#     Lecture 13     #
######################


# Task 1

#This program has a problem!
donuts = eval(input("Aaron, Beth, and Cody go out for donuts." + \
                    "How many donuts do they buy?: "))

while donuts >= 3 :
    print("Aaron takes a donut.")
    print("Beth takes a donut.")
    print("Cody takes a donut.")
    donuts -= 3
    print("There are", donuts, "left!")	#Here we trace!


print("They took all the donuts!")

print()

#----------------------------------------------------------------------

# Task 2

while True:
    
    file_search = input("Please enter a file name or STOP: ")
    
    if file_search.lower() != "stop":
        
        file = open(file_search, "r")
        lines = file.readlines()
        file.close()

        num_of_lines = len(lines)

        print(file_search, "has", num_of_lines, "lines of data in it!")
        print()
        
    else:
        
        break

print()

#----------------------------------------------------------------------

# Task 3

numbers = []

while True:
    
    number = input("Please enter a number or STOP: ")

    if number.lower() == "stop":
        total = sum(numbers)
        print("The total sum is", total)
        break

    numbers.append(eval(number))
