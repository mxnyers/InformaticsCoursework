#Homework 6

print("Homework 6")

print()

print("6.20")

print()
#Function that will swap the term and definition in each variable the dictionary
def reverse(dictionary):
    for i in dictionary:
        print({dictionary[i] :i})

#A dictionary of names and numbers that will be switched after the function is complete
phonebook = {"Smith, Jane": "123-45-67", "Doe, John": "987-65-43", "Baker, David": "567-89-01"} 

#Print statements that show what the function will do after it is run
print("Before: ")
print(phonebook)
print()
print("After: ")
print(reverse(phonebook))

print()


print("6.22")

print()

#function that takes a word and shows what it would look like in a mirror

def mirror(word):
    mir_dict = {"b": "d", "d": "b", "o": "o", "p": "q", "q": "p", "v": "v", "w": "w", "x": "x"}
    empty = ""
#For loop that will check each individual letter within a word
    for letter in word:

#If statement that checks to see if the letter is in the dictionary and will add the reversed letter to the string if it is 
        if letter in mir_dict:
            empty += mir_dict[letter]

#Else statement that will return invalid if the letter is not in the dictionary
        else:
            return "INVALID"
    return empty
#print statements that showcase the functions capabilities
print("mirror('vow')")
print(mirror("vow"))
print()

print("mirror('wood')")
print(mirror('wood'))
print()

print("mirror('bed')")
print(mirror('bed'))
print()


print("6.24")

print()

#Function that will ask the user for a name input it into an empty dictionary and use the dictionary to count how many times the user enters a specefic name
def names():
    names_dict = {}
    name = " "

#While statement that is testing to see if the user breaks the code and if they don't it loops the program until they do
    while name != "":
        name = input("Enter next name: ")

#If/else statement that tests to see if the input is in the list and if it isn't it will add it to the list and begin counting
        if name in names_dict:
            names_dict[name] += 1
        else:
            names_dict[name] = 1

#Delete function that removes the empty variable set in the beginning
    del names_dict[""]

#For statement that goes through each item in the final form of the dictionary and prints out the results
    for k in names_dict:
            print("There are", names_dict[k], "student(s) named", k  + ".")

#calling upon the function
names()       
print()

print("6.28")

print()

#Function that will take a small amount of words and translate them into spanish
def translate(dictionary):

#While loop that loops the program until the term is not found in the dictionary
    while True:
        word_trans = input("Please enter a word to translate into spanish: ")

#If statement that will test to see if the term is in the dictionary and if it is not it will end the program
        if word_trans not in dictionary:
            print("___.")
            break

#Else statement that will return the translated word to the user and ask for a new word after wards
        else:
            print("The translated word is,", dictionary.get(word_trans))
        
#Dictionary of different words from english to spanish
translation = {"Hello": "Hola", "Bye": "Adios", "I": "Yo", "You": "Tu"}        

#Calling on the function
translate(translation)
        
print()

print("6.33")

print()

#Imports the random module
import random

#Function that will see how many rolls it takes to get to 100 rolls of a number
def diceprob(r):
    tot = 0
    count = 0
    r = int(r)

#While loop that repeats until the value is 100
    while count < 100:

#Using the random range function to generate random rolls for two 6 sided dice
        roll = random.randrange(1, 7) + random.randrange(1, 7)

#Counting function for each roll
        tot += 1

#If statement that will see if each roll equals the user's number and if it does it adds it to the number's count
        if roll == r:
            count += 1

#If statement that will break the code and return the total rolls and number of times the user's number got rolled when it hitss 100            
        if count == 100:
            print("It took", tot, "rolls to get", count, "rolls of", str(r) + ".") 
            break
diceprob(4)   
print()
