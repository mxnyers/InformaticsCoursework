#Lab Practical 1

#Calling upon the donation module
import donation

# main

# Section 1 - get all of the donations and output the values

# As an example of how to get an amount, this gets 1 donation and prints it out
# Run the program a few times and notice that the amount changes.
# If the code won't run, did you put this file and donation.py in the same directory?

print()

#This for loop generates 200 random donation amounts and puts them into a list
total_donation = []
for i in range(200):
    total_donation.append(donation.get_donation())
print("The donation amounts:", total_donation)

#This code puts the donations in order
print("The donations in order:", sorted(total_donation))

#This code provides empty space
print()

# Section 2 - Compute basic categories

#This code will calculate the number of small donations
small = 0
for amount in total_donation:
    if amount <= 5:
        small += 1
        
print("There were", small, "small donations ($5 or less).")

#This code will calculate the number of medium donations
medium = 0
for amount in total_donation:
    if 5 < amount <= 15:
        medium += 1

print("There were", medium, "medium donations ($6 - $15).")

#This code will calculate the number of large donations
large = 0
for amount in total_donation:
    if amount >= 16:
        large += 1

print("There were", large, "large donations ($16 or more).")

print()

# Section 3 - Compute success or failure

#This for loop will calculate the total amount of money raised
total_amount = 0
for amount in total_donation:
    total_amount += amount
print("The total amount of money raised is:", total_amount)

#This if statement will let the user know if enough money was raised to meet the goal
if total_amount >= 2017:
    print("The fundraising goal was met!")
else:
    print("The fundraising goal was not met.")

print()

# Section 4 - What can you expect from the bank?

#This code is the print function needed to reiterate the statement
print("The bank cashed this amount as: ")
print("----------------------------------")


#Calculations checking to see if the various functions are divisible by the various bill amounts
hundred = total_amount // 100
total_amount = total_amount - (100 * hundred)

twenty = total_amount // 20
total_amount = total_amount - (20 * twenty)

ten = total_amount // 10
total_amount = total_amount - (10 * ten)

five = total_amount // 5
total_amount = total_amount - (5 * five)

one = total_amount // 1
total_amount = total_amount - (1 * one)
#This print function calls upon the variables to show the various dollar amounts
print("$100 bills:", hundred)
print("$20 bills:", twenty)
print("$10 bills:", ten)
print("$5 bills:", five)
print("$1 bills:", one)


    









        
