# HOMEWORK 3


# 3.20

#print to signify which problem it is and to leave smome space in between the problem number and the aproblem itself
print("3.20")

#variable that signifies the first 3 months of the year
lst = ['January', 'February', 'March']

#for loop that is checking each string in the list and printing the first 3 characthers of that string
for word in lst:
    print(word[:3])

print("")

#3.25
print("3.25")

#User input and list of letters the names can start with if the name can be printed
user_names = eval(input("Enter a list of names: "))
first = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

#for loop testing to see which names can be printed and prints them
for name in user_names:
    if name[0] in first:
        print(name)

print("")

#3.41
print("3.41")

#Function that takes the users last and first names and reorrganizes it in a new way
def lastF(FirstName, LastName):
    FirstName = input("First Name: ")
    LastName = input("Last Name ")
    FullName = (LastName + ", " + FirstName[0] + ".") 
    return FullName

#Print function that explauins what the new function will do and provides an example
print("The function, lastF(), will shift your name in a new way if you in put like so, lastF(First, Last), then reenter the name when asked. For example: ")

print("lastF('Albert', 'camus') =", lastF("Albert", "Camus"))

print("")

#3.44
print("3.44")

#print function telling the user what to do
print("In the section below please put an input in the form of distance(seconds) to calculate the distance of a lightning strike. For example: ")

#function that takes seconds and calculates how far away a lightning strike is from the user
def distance(seconds):
    dis = (seconds * 340.29) / 1000 
    return dis

#print function that is giving the user an example of how to calculate the distance
print("distance(3) =", distance(3))

print("")

#Random Cinema
print("Random Cinema")

#importing the random module
import random

#Function that will 3 random movie names
def ranMov(names):
    movie_num = eval(input("Please enter the number of movies you want to see: "))

#For loop that takes the user input and generates that amount of movie names
    for i in range(movie_num):
        print(random.choice(names), random.choice(names), random.choice(names))

#Asking for a user input of random words to help generate a list
ranMov(eval(input("Please enter a list of words: ")))    
      
