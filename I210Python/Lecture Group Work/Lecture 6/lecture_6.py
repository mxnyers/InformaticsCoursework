message = input("Please enter a string in lowercase: ")
target = input("What letter are you looking for? ")

counter = 0

for letter in message :
    if letter == target :
        counter += 1

print("I found", target, counter, "times.")
'''

'''
message = input("Please enter a string in lowercase: ")
target = input("What letter are you looking for? ")

counter = 0

for i in range(len(message)) :
    if message[i] == target :
        counter += 1
        print(target, "found at position", i)

print("I found", target, counter, "times.")


string = input("Please enter some text: ")
new_string = ""

for letter in string :
    if letter not in "aeiou" :
        new_string += letter
        new_string = new_string + letter

print(new_string)
