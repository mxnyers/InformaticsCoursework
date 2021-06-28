#------------
# Problem 1
#------------

python_words = {"string": "a sequence of characters", \
                   "int": "a whole number (integer) "}

#add your code here

# Keep looking up or adding key/values until the user wants to
# stop
while True:

    # Ask the user for a key to look up
    prompt = input("Enter a key or stop to exit: ")
    print()

    # If the user enters "stop" exit the program
    if prompt.lower() == "stop":
        break

    # If the user enters a key that is not in the dictionary,
    # state that they key was not found and add the key with
    # the definition/value that user enters
    if prompt not in python_words:
        
        print("Not Found")
        python_words[prompt] = input("Enter a definition for " \
                                     "this key: ")
        print()

    # Print the definition/value of the key
    print(python_words[prompt])
    print()

#------------
# Problem 2
#------------

# Define a table of player scores
scores = {"Dan" : 125, "Abby" : 100, "Carrie" : 275, "Ben" : 150}

# List the players
print("Current Players:")
print(" ".join(sorted(scores.keys())))
print()

# Ask the user which player score should be displayed
lookup = input("Please enter a Player Name: ")

# Print the players score or "not found" if the player is not in the table
print("The score for", lookup.title(), "is", scores.get(lookup.title(), "not found"), ".")
