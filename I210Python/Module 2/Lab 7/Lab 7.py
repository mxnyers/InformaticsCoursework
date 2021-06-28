#Lab 7

print("Lab 7")

print()

#Part 1
print("Part 1:")

#Opens up a text file and reads its contents line by line

with open("INCounties2015.txt", "r") as f:
    file_contents = f.readlines()
    
for i in range(len(file_contents)):
    file_contents[i] = file_contents[i].strip().split("\t ")




counties = {}

#For loop that will unpack the list made from the read text file and put them into a dictionary
for entry in file_contents:
    counties[entry[0]] = int(entry[1].replace(",", ""))

print(counties)

print()

#Part 2
print("Part 2:")

#Printing out all of the counties that were originally a list but . join turns them into strings
print("The counties in Indiana are:")
print(", ".join(sorted(counties.keys())), "\n")

print("The population of Monroe county as of 2015 was:", counties.get("Monroe",0))
print("The total IN population as of 2015 was:", sum(counties.values()))
print("So Monroe County acounts for",( counties.get("Monroe",0)/ sum(counties.values()) * 100),\
      "% of IN's population")
