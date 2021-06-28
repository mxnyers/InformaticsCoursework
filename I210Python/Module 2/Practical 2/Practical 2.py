from tools import *

#With function that will open and read each individual line of the state of California's results until the list ends and it will close automatically
with open("california.txt", "r") as j:
    cal_result = j.readlines()

#With function that will open and read each individual line of the state of Texas's results until the list ends and it will close automatically
with open("texas.txt", "r") as k:
    tex_result = k.readlines()

#Section 1

cthulu_Ccalc = 0 
doom_Ccalc = 0
zilla_Ccalc = 0
joker_Ccalc = 0
vold_Ccalc = 0

cthulu_Tcalc = 0 
doom_Tcalc = 0
zilla_Tcalc = 0
joker_Tcalc = 0
vold_Tcalc = 0

for i in range(len(cal_result)):
    cal_result[i] = cal_result[i].strip().split("\t")

for entry in cal_result:
    if entry[0] == "Cthulu":
        cthulu_Ccalc += int(entry[1])
    if entry[0] == "Godzilla":
        zilla_Ccalc += int(entry[1])
    if entry[0] == "Dr. Doom":
        doom_Ccalc += int(entry[1])
    if entry[0] == "Voldemort":
        vold_Ccalc += int(entry[1])
    if entry[0] == "The Joker":
        joker_Ccalc += int(entry[1])
    

for l in range(len(tex_result)):
    tex_result[l] = tex_result[l].strip().split("\t")

for entry in tex_result:
    if entry[0] == "Cthulu":
        cthulu_Tcalc += int(entry[1])
    if entry[0] == "Godzilla":
        zilla_Tcalc += int(entry[1])
    if entry[0] == "Dr. Doom":
        doom_Tcalc += int(entry[1])
    if entry[0] == "Voldemort":
        vold_Tcalc += int(entry[1])
    if entry[0] == "The Joker":
        joker_Tcalc += int(entry[1])
   
        

cal_tot = {"Dr. Doom": doom_Ccalc, "Godzilla": zilla_Ccalc, "The Joker": joker_Ccalc, "Voldemort": vold_Ccalc, "Cthulu": cthulu_Ccalc}

tex_tot = {"Dr. Doom": doom_Tcalc, "Godzilla": zilla_Tcalc, "The Joker": joker_Tcalc, "Voldemort": vold_Tcalc, "Cthulu": cthulu_Tcalc}
    
state = input("Which state's totals would you like to compute? ")

if state.title() == "California":
    print(cal_tot)

if state.title() == "Texas":
    print(tex_tot)


#Section 2

state = input("Which state's totals would you like to compute (Texas or California)? (or STOP) ")

while True:
        if state.title() == "California":
            print(cal_tot)

        if state.title() == "Texas":
            print(tex_tot)
        else:
            break

#Section 3

nest = []


nest = list(cal_tot)
sorted_nest = [nest.pop()]

print(cal_tot)
print(tex_tot)
while nest:
    current = nest.pop()
    for n in range(len(sorted_nest)):
        if current[1] > sorted_nest[n][1]:
            sorted_nest.insert(n, current)
            current = ""
            break
    if current:
        sorted_nest.append(current)
table_print(["Name", "Votes"], sorted_nest, 15)
print(nest)


#I ran out of time for comments and the second half of problem 3
