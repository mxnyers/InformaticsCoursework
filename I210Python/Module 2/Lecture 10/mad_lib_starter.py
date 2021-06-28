######################
#     Lecture 10     #
######################


# Task 1

# set up the mad lib with placeholders marked with "_"
mad_lib = """
In the book War of the _noun1_, the main character is an anonymous _occupation_
who records the arrival of _animals_ in _place_. Needless to say, havoc reigns as
the _animals_ continue to _verb_ everything in sight, until they are killed by
the common _noun2_.
"""

# get input from the user - tell them what it needs to be!
noun1 = input("Please enter a plural noun: ")
occupation = input("Please enter an occuptaion: ")
animals = input("Please enter a plural word for an animal: ")
place = input("Please enter a place: ")
verb = input("Please enter a verb: ")
noun2 = input("Please enter a second noun: ")

# replace all of the placeholders with user input.
# the first noun and the place need to have their
# first letters capitalized
mad_lib=mad_lib.replace("_noun1_", noun1.title())
mad_lib=mad_lib.replace("_occupation_", occupation)
mad_lib=mad_lib.replace("_animals_", animals)
mad_lib=mad_lib.replace("_place_", place.title())
mad_lib=mad_lib.replace("_verb_", verb)
mad_lib=mad_lib.replace("_noun2_", noun2)

# print the resulting mad lib
print(mad_lib)

print()

#---------------------------------------------------------------------

# Task 2

message = input("Please enter a message: ")
message_list = message.split(" ")

print("That message has", len(message_list),"words.")

largest_word = ""

for word in message_list:
    if len(word) > len(largest_word):
        largest_word = word

print("The longest word was:", largest_word)

print()

#----------------------------------------------------------------------

# Task 3

message = input("Please enter a message: ")

for i in range(len(message)):
    print(message[:i + 1])
