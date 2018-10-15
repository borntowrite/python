class Animal:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs
    def getLegs(self):
        return "{0} has {1} legs".format(self.name, self.legs)
    def says(self):
        return "I am an unknown animal"

class Dog(Animal): # <Dog inherits from Animal here (all methods as well)
    def says(self): # <Called instead of Animal says method
        return "I am a dog named {0}".format(self.name)

formless = Animal("Animal", 0)
rover = Dog("Rover", 4) #<calls initialization method from animal

print(formless.says()) # <calls animal say method
print(rover.says()) #<calls Dog says method
print(rover.getLegs()) #<calls getLegs method from animal class