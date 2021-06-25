######################
#     Lecture 12     #
######################

import os

# Task 1
text_file = open("test.txt", "r")

file_contents = text_file.read()

print(file_contents)

text_file.close()

print()

#--------------------------------------------------

# Task 2
# Store the contents of the file into a list
number_file = open("numbers.txt", "r")
numbers = number_file.readlines()
number_file.close()

# Add up the numbers in the list
total  = 0
for num in numbers:
    total += int(num)

# Display the total
print("The total is:",total)

print()

#---------------------------------------------------

# Task 3
def copy_file(filename_from, filename_to):
    copy = open(filename_from, "r")
    contents = copy.read()
    copy.close()

    paste = open(filename_to, "w")
    paste.write(contents)
    paste.close()

#testcode
file_f = input("Please enter the name of the file to copy FROM: ")
file_t = input("Please enter the name of the file to copy TO: ")

copy_file(file_f , file_t)

print("The content of", file_f, "has been copied into", file_t, ".")

print()

#---------------------------------------------------------------------------

# Task 4
print("This program prints out all the .txt files in the print directory.")
print("Current directory's text files:")

sample_dir = os.listdir(os.getcwd())
txt_files = []

for file in sample_dir:
    if "txt" in file:
        txt_files.append(file)

print(txt_files)
