""""
Justin Choi
IDT Period 3
11 January 2023
Dogs Class
"""


class Dogs():
    
    #Constructor for the Princess Class
    def __init__(self, dogName, dogBreed, dogAge): 
        self.dogName = dogName
        self.dogBreed = dogBreed
        self.dogAge = dogAge
    
    def getDogName(self):
        #user validation gets here
        return self.dogName

    def setDogName(self, dogName):
        #user validation gets here
        self.dogName = dogName
    
    def getDogBreed(self):
        #user validation gets here
        return self.dogBreed

    def setDogBreed(self, dogBreed):
        #user validation gets here
        self.dogBreed = dogBreed
    
    def getDogAge(self):
        #user validation gets here
        return self.dogAge

    def setDogAge(self, dogAge):
        #user validation gets here
        self.dogAge = dogAge
        
    def displayDog(self):
        print("Dog Analyzer")
        print("{} the {} is {} years old.".format(self.getDogName(), self.getDogBreed(), self.getDogAge()))