# Table Print v2

#----------------------
# Function Definitions
#----------------------

def table_print(headers, data):

    # Add your code here!

    for header in headers:
        print(header, end = "\t")

    print()
    print("-" * 25)

    for i in range(len(data)):
        print(i, data[i][0], data[i][1], sep = "\t")

    # Nothing else in the file should change


def table_print2(headers, data, width):

    # Add your code here!

    output = "{:>{}} {:>{}}"
    
    print(output.format(headers[0], width, headers[1], width))

    print("-" * (width + 1) * 2)

    for record in data:
        print(output.format(record[0], width, record[1], width))

    # Nothing else in the file should change

#-------------------------------------------------------------------------

#-------------------------------
#main - Don't change this part!
#-------------------------------

labels = ["i", "Name", "Score"]
scores = [("Abe", 200), ("Bill", 180), ("Mary", 215)]

table_print(labels, scores)

print()

labels2 = ["i", "Capital", "State"]
state_data = [("Atlanta", "GA"), ("Boise", "ID"), ("Boston", "MA"), ("Austin", "TX")]

table_print(labels2, state_data)

print()

#-------------------------------------------------------------------------------------
    
labels = ["Name", "Score"]
scores = [("Abe", 200), ("Bill", 180), ("Mary", 215)]

table_print2(labels, scores, 6)

print()

labels2 = ["Capital", "State"]
state_data = [("Atlanta", "GA"), ("Boise", "ID"), ("Boston", "MA"), ("Austin", "TX")]

table_print2(labels2, state_data, 8)
