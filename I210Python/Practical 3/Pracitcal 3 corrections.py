#Practical 3 Corrections

class Place(object):

    locations_list = []
    
    def __init__(self, name, location = None):
        self.__name = name
        self.__location = None
        self.__visited = False
        Place.locations_list.append(self)
        print(name,"has been visited! \n")

    def __str__(self):

        out = self.get__name() + "\n"
        out += "is located at " + str(self.__location) + "\n"

        if not self.get__location():
            out += "is located at " + self.get__location.get__name()
            
        if self.get__visited():
            out += " and has been visited \n"

        else:
            out += " and has not been visited \n"
        return out

    def get__name(self):
        return self.__name

    def get__location(self):
        return self.__location

    def get__visited(self):
        return self.__visited

    def visit(self):
        if self.get__visited():
            print(self.get__name, "has already been visited \n")

        else:
            self.__visited = True
            print(self.get__name(), "has been visited. \n")
            if self.get__location() != None:
                self.get__location().visit()

    @staticmethod
    def locations():
        for location in Place.locations_list:
            print(location)

class Home(Place):

    def __init__(self, name, bedrooms, occupancy, location = None):
        super().__init__(name, location)
        self.__bedrooms = bedrooms
        self.__occupancy = occupancy

    def __str__(self):
        out = super().__str__()
        out += "It has " + str(self.get__bedrooms()) + " bedrooms \n"
        out += "It has " + str(self.get__occupancy()) + " occupants \n"
        return out


    def get__bedrooms(self):
        return self.__bedrooms

    def get__occupancy(self):
        return self.__occupancy

class City(Place):

    def __init__(self, name, mayor, population, location = None):
        super().__init__(name, location)
        self.__population = population
        self.__mayor = mayor

    def __str__(self):
        out = super().__str__()
        out += "It has " + str(self.get__mayor()) + " as mayor \n"
        out += "It has a population of " + str(self.get__population()) + " people \n"
        return out


    def get__mayor(self):
        return self.__mayor

    def get__population(self):
        return self.__population


#Main

iu = Place("IU Campus")
library = Place("Wells Library", iu)
print(iu)
print(library) 

indiana = Place("Indiana")
indy = City("Indianapolis", "Joseph Hogsett", 853173, indiana)

btown = City("Bloomington", "John Hamilton", 80405, indiana)
rental = Home("Rental House", 5, 4, btown)
historic = Home("Elias Abel House", 4, 0, btown)
#Place.locations()
print("-"*100)
rental.visit()
Place.locations()
