#Homework 4
print("Homework 4")

print()

#4.13
print("4.13")

print()

s = "abcdefghijklmnopqrstuvwxyz"

#boolean conditions testing to see if the different slices are the same as the other strings
print("(a)", s[1:3] == "bc")

print("(b)", s[:14] == "abcdefghijklmn")

print("(c)", s[14:] == "opqrstuvwxyz")

print("(d)", s[1:25] == "bcdefghijklmnopqrstuvwx")

print()

#4.16
print("4.16")

print()

#Gathering a user input for three words
first = input("Enter first word: ")
second = input("Enter second word: ")
third = input("Enter third word: ")

#variable that puts all the words into a list
words = [first, second, third]

#Boolean condition that tests to see if the words are in alphabetical/dictionary order and will print true if it is true and will print a blank line if it is false
if words == sorted(words):
    print("True")
else:
    print()


print()

#4.20
print("4.20")

print()

sender = "tim@abc.com"
recipient = "tom@xyz.com"
subject = "Hello!"

#Formatting of the email that is going to be sent
print( "From:", sender, "\nTo:", recipient, "\nSubject:", subject)


print()

#4.23
print("4.23")

print()

#Taking input from user
sample = input("Enter a sentence: ")

#Splitting up the input into a list
terms = sample.split()

#Taking the average of the length of each word
avg = sum(len(term) for term in terms)/(len(terms))

print(avg)


print()

#4.25
print("4.25")

print()

#Function that takes an input and calculates the number of vowels in a sentence
def vowelCount(sentence):
    sentence = sentence.lower()
    vwls = {'a':0, 'e':0, 'i':0, 'u':0, "u":0}
    for letter in sentence:
        if letter in vwls:
            vwls[letter] += 1
    return vwls

print("vowelCount('Le Tour De France')")

#Formatted print statement that shows the user the number of vowels entered in the sentence
print("a, e, i, o, u, appear, respectively,", vowelCount("Le Tour De France"), "times")


        

print()
