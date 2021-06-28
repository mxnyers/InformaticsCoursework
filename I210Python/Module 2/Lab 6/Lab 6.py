###Lab 6

###Part 1

##while number < 100:

##Part 2
##
##while username != "":
###or
##while True:
##
##    username = input("Please enter your name: ")
##
##    if username:
##        break
##
##print("Your username is: ", username)

###Part 3
##
##while cars != int(cars):

###Part 4
##
##hand = []
##
##while True:
##    card = eval(input("Please enter a card value: "))
##    hand.append(card)
##    if sum(hand) >= 21 or len(hand) == 3:
##        break
##
##print("Your final hand is:", hand) 
##
##if sum(hand) == 21:
##    print("The value is:", sum(hand))
##    print("Perfect!")
##
##if sum(hand) > 21:
##    print("The value is:", sum(hand))
##    print("Too high!")
##
##if sum(hand) < 21:
##    print("The value is:", sum(hand))
##    print("Not bad!")

#Part 5

text_file = open("top100moviesRT.txt", "r")
file_contents = text_file.readlines()
text_file.close()
for i in range(len(file_contents)):
    file_contents[i] = file_contents[i].strip()

print("The file 'top100moviesRT.txt' has been loaded. \nIt contains the top 100 movies of all time according to Rotten Tomatoes")
while True:
    movie = input("Please enter a movie title (or STOP): ").title()
    if movie.lower() == "stop":
        break
    if movie in file_contents:
        print("Thats the #", file_contents.index(movie)+ 1, "of all time.")
    else:
        print("I couldn't find that movie in the list.")
    
    

