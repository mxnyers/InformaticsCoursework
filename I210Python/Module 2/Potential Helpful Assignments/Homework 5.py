#Homework 5

#5.29
print("5.29")

#Function that will print the two separate lists when called upon
def lastfirst(LastName, FirstName):
    print([FirstName, LastName])

#User inputs that will be used in the function
LastName = eval(input("Please enter a list of last names: "))
FirstName = eval(input("Please enter a list of first names: "))

#Function that calls upon two separate lists and puts them together
lastfirst(LastName, FirstName)

print()

#5.39
print("5.39")

#Variable that encloses all of the vowels
vowels = ["a", "e", "i", "o", "u"]

#Function that will take any word and if it has any vowels it will multiply the vowel by 4 and add an exclamation point to make the phrase seem more like shouting 
def exclamation(word):
    for letter in vowels:
            word = word.replace(letter, letter*4)
    return word + "!"
#print statements that showcases the functions capabilities 
print("exclamation('argh')" ) 
print(exclamation('argh'))
print("exclamation('hello')")
print(exclamation('hello'))

print()

#5.43
print("5.43")

#Function that will take each row of the list and test it to see if the sum is odd or even and will say so by true or false
def evenrow(number_list):
    for i in number_list:
        if sum(i) % 2 == 1:
            return False
    return True

#Print statements that showcases the functions capabilities
print("evenrow([[1,3], [2,4], [0,6]])")
print(evenrow([[1,3], [2,4], [0,6]]))
print("evenrow([[1,3,2], [3,4,7], [0,6,2]])")
print(evenrow([[1,3,2], [3,4,7], [0,6,2]]))
print("evenrow([[1,3,2], [3,4,7], [0,5,2]])")
print(evenrow([[1,3,2], [3,4,7], [0,5,2]]))
