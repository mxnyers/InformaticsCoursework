#Practical 3

#Original Class
class Place(object):
        #Static Method that will test to see if there are any locations inside the list and if there are any it will print them out
	@staticmethod
	def locations():
		loc_plc = []
		if len(loc_plc) >= 1:
			print("The following locations exist: \n")
		else:
			print("No locations exist at this time. \n")
		for area in loc_plc:
			print(area)
			
	def __init__(self, name, location, visited):
		print(name, "Created. \n")
		self.__name = name
		self.__location = None
		self.visited = False
	def __str__(self):
			reply = ""
			reply += self.__name + ","
			if self.__location == None:
				reply += " "
			else:
				reply += " located in" + self.__location
			if self.visited == False:
				reply += "(not visited). \n"
			else:
				reply += "(Visited). \n"
			return reply
	def visit():
			self.visited = True
			print("You visit", self.__name + ".")
			print("That means... You visit", self.__name + ".")
			print("That means... You visit", City.city + ".")
			print("That means... You visit", City.state + ".")
#Child Class	
class Home(Place):
	def __init__(self, company, city, bedrooms, occupancy,):
		self.company = company
		self.city = city
		self.occupancy = int(occupancy)
		self.bedrooms = int(bedrooms)
	def __str__(self):
			super().__str__(self)
			reply += "This house has " + self.bedrooms + " bedrooms, of which " + self.occupancy + "are occupied."
			return reply
#Child Class
class City(Place):
	def __init__(self, city, state, population, mayor):
		self.city = city
		self.state = str(state)
		self.population = int(population)
		self.mayor = str(mayor)
	def __str__(self):
			super().__str__(self)
			reply += "This city has " + self.population + " residents, and the mayor is " + self.mayor + "."
			return reply

#Main

#Section 1
iu = Place("IU Campus", None, False)
library = Place("Wells Library", iu, False)

#Section 2				
Place.locations()
print(iu)
print(library)
Place.locations()

#Section 3
Place.locations()

indiana = Place("Indiana", None, False)
indy = City("Indianapolis", indiana, 853173, "Joeseph Hogsett")

Place.locations()
print(indy)

