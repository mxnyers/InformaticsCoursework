##rows = eval(input("How many rows should we have? "))
##cols = eval(input("How many columns should we have? "))
##
##for i in range(rows):
##    print("Row", i, ":", end = " ")
##
##    for j in range(cols):
##        print(j, end = " ")

##    print()

#Multiplication Table
for i in range(0,11):
    
    for j in range(0,11):
        if i == 0 and j == 0:
            print("*", end = "\t")
        elif i == 0:
            print(j, end = "\t")
        elif j == 0:
            print(i, end = "\t")
        else:
            print(i*j, end="\t")
        
    print()
