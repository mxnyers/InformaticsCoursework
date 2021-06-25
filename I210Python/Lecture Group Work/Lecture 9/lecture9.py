### function definitions
##def dasher(string):
##
##    # Join the elements of the string variable as string with a dash between each element.
##    # Append a dash to either side of the new joined string.
##    dashed_string = "-" + "-".join(list(string)) + "-"
##
##    return dashed_string
##
##def dasher2(string) :
##
##    # Check if the string variable is a valid length. If not, set string equal to "Error"
##    if len(string) > 20 :
##        string = "Error"
##    
##    # Append an even number of dashes (if possible) to either side of the string variable
##    # First, calculate how many dashes when be appended
##    remaining_space = (20 - len(string))
##    num_dashes = int(remaining_space / 2)
##
##    # If the length of the string variable is an odd number, the number dashes
##    # on either side of the string will not be even. If this is the case, add
##    # an extra dash to the end of the string
##    if len(string) % 2 == 0 :
##        dashed_string = "-" * num_dashes + string + "-" * num_dashes
##    else :
##        dashed_string = "-" * num_dashes + string + "-" * num_dashes + "-"
##
##    return dashed_string

def dasher3(string, length = 20) :

    # Check if the string variable is a valid length. If not, set string equal to "Error"
    if len(string) > length :
        string = "Error"
    
    # Append an even number of dashes (if possible) to either side of the string variable
    # First, calculate how many dashes when be appended
    remaining_space = (length - len(string))
    num_dashes = int(remaining_space / 2)
    dashed_string = "-" * num_dashes + string + "-" * num_dashes

    # If the length of the string variable is an odd number, the number dashes
    # on either side of the string will not be even. If this is the case, add
    # an extra dash to the end of the string
    if len(string) % 2 == 0 :
        dashed_string
    else :
        dashed_string += "-"

    return dashed_string

print(dasher3("Hello"))
print(dasher3("Hello", 67))

### main section of the program
##print(dasher("Hello"))
##print(dasher("Greetings"))
##print(dasher(dasher("TEST?")))
##
##print()
##
##print(dasher2("Hello"))
##print(dasher2("Welcome"))
##print(dasher2("Boom"))
##print(dasher2("This is a super long test"))


