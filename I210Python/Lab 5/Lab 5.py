dinosaurs = [["Tyrannosaurus", 16000, "Carnivore", "Last Cretaceous"],
             ["Ankylosaurus", 10000, "Herbivore", "Last Cretaceous"],
             ["Stegosaurus", 6000, "Herbivore", "Last Jurassic"],
             ["Deinonychus", 175, "Carnivore", "Early Cretaceous"]]

output = "{0:20} {1:15} {2:15} {3:20}"
headers = ["Name", "Weight", "Diet", "Time"]
print(output.format("Name", "Weight (lbs)", "Diet", "Time"))
print("-" * 70)

for dino in dinosaurs:
    name, weight, diet, time = dino
    print(output.format(name, str(weight), diet, time))



def table_print(headers, data, width):

    output = "{:<{}} {:<{}}"
    
    print(output.format(headers[0], width, headers[1], width))

    print("-" * (width + 1) * 2)

    for record in data:
        print(output.format(record[0], width, record[1], width))

nest = []

headers = ["Nest", "Eggs"]
for i in range(4):
    dino = input("Please enter the dinosaur's name: ")
    eggs = input("Please enter how many eggs were found: ")
    print("Current fossilized dinosaur egg count:\n")
    nest.append((dino, eggs))
    table_print(headers, nest, 20)
    print()
    
