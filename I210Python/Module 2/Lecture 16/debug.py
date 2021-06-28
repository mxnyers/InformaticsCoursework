##def vowel_count(string):
##    count = 0
##    y_count = 0
##
##    for letter in string:
##        if letter.lower() in vowels:
##            count += 1
##        elif letter.lower() == "y":
##            y_count += 1
##
##    return count, y_count
##
###main
##vowels = ["a", "e", "i", "o", "u"]
##
##message = "This is a test message. This is only a test. Only!"
##
##total, ys = vowel_count(message)
##print("The message has", total, "vowels in it.")
##print("It also has", ys, "ys in it.")


# Task 2
with open("professions.txt", "r") as f:
    professions = f.readlines()

records = []

for person in professions:
    records.append(person.strip().split(", "))

##for record in records:
##    print(record)
##print()

##print("All the data:")

# Task 3
sorted_records = [records.pop()]

while records:
    record = records.pop()
    for i in range(len(sorted_records)):
        if int(record[1]) < int(sorted_records[i][1]):
            sorted_records.insert(i, record)
            record = ""
            break

    if record:
        sorted_records.append(record)
    
for record in sorted_records:
    print(record)

##print(records)
