# Task 1

# Completed in class on paper




# Task 2

# Create an empty list
desserts = []

# Ask the user for their favorite desserts and append them to the desserts list
desserts.append(input("Please enter your favorite dessert: "))
desserts.append(input("Please enter your second favorite: "))
desserts.append(input("Please enter your third favorite: "))

# Print the values in the desserts list
print("Your list is: " + str(desserts))

# Check if 'Pie' is in the desserts list and return True or False
# Capitalization DOES matter!
print("One of your favorite desserts is 'Pie': " + str("pie" in desserts))

# Sort the list in alphabetical order and display the result
desserts.sort()
print(desserts)




# Task 3

# Ask the user for a phrase
phrase = input("Please enter a phrase: ")

# Ask the user for index positions and store them in first, second, and third_index
#
# WARNING: if the user enters a number that is greater than the largest index position of
# the phrase or if the user enters a non-numeric value, you will get a Traceback error
first_index = int(input("Please enter the first index position: "))
second_index = int(input("Please enter the second index position: "))
third_index = int(input("Please enter the third index position: "))

# Combine the characters at each of the index positions in the phrase from the beginning
# and store the result in new_phrase
new_phrase = phrase[first_index] + phrase[second_index] + phrase[third_index]

# Display the result
print("Those three index positions in that phrase, put together, are: " + new_phrase)
