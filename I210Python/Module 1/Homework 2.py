print("Homework 2")

print("3.19")

a, b, c = 3, 4, 5


if a < b:
    print("A. OK")
else:
     print("A. NOT OK")


if c < b:
    print("B. OK")
else:
    print("B. NOT OK")


if a + b == c:
    print("C. OK")
else:
    print("C. NOT OK")


if (a**2) + (b**2) == (c**2):
    print("D. OK")
else:
     print("D. NOT OK")


print("3.24")

security = eval(input("Enter list of words: "))

for word in security:
    if word != "secret":
        print(word)
        

print("3.30")

print("This program will average out a list of 3 numbers and compare it to the last number for you!")

first = int(input("Please input the first number: "))
second = int(input("Please input the second number: "))
third = int(input("Please input the third number: "))
last = int(input("Please input the last number: "))

avg = (first + second + third)/3
if avg == last:
    print("Equal ")
else:
    print("Not Equal")


print("3.34")

print("This program will calculate your pay for the current pay period. Please enter your hours and wages as the following function: pay(wage, hours).")

def pay(wage, hours):
    total = hours * wage
    if hours > 40:
        ot = hours - 40
        total += ((ot) * (.5 * wage))
    return total








