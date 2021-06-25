#################
#     Lab 4     #
#################



# TASK 1

# Define variables used in for loops
client_countries = []
test_scores = []
names = ["chris", "nora", "joe"]


# Question 1
for country in client_countries :
    # Do something
    continue

# Question 2
for i in range(10) :
    # Do something
    continue

# Question 3
for score in test_scores :
    # Do something
    continue

# Question 4
# Option 1
for name in names :
    print(names.index(name))
print()

# Option 2
for i in range(len(names)) :
    print(i)
print()

# If a problem asks to return an INDEX, you will most likely need to use i and range()
# in your for loop.



# TASK 2

# Question 1
# Define function
def zero_counter(num_list) :
    num_of_zeroes = 0
    for num in num_list :
        if num == 0 :
            num_of_zeroes += 1
            
    return num_of_zeroes


# Main
my_nums = [0,0,0,1]

print(zero_counter(my_nums))
print()

# Question 2
def common_name(names) :
    return name

# Question 3
def max_and_min() :
    return largest, smallest



# TASK 3

# Define functions
# Question 1
def min_and_max() :

    user_list = eval(input("Please enter a list of numbers: "))

    largest = max(user_list)
    smallest = min(user_list)

    return largest, smallest

# Question 2
def most_frequent(names) :
    largest = 0
    freg_name = ""

    for name in names :
        if names.count(name) > largest :
            largest = names.count(name)
            freq_name = name

    return freq_name


# Main
group = ["chris", "chris", "joe", "nora"]

minimum, maximum = min_and_max()

print("The largest number is " + str(maximum))
print("The smallest number is " + str(minimum))
print()

print("Most commmon name: " + most_frequent(group))
print()
