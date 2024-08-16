"""
Justin Choi
IDT Period 3
12 January 2023
Container
"""



class Human():
    
    #Constructor for the Human Class
    def __init__(self, humanName, humanHeight, humanIq): 
        self.humanName = humanName
        self.humanHeight = humanHeight
        self.humanIq = humanIq
    
    def getHumanName(self):
        #user validation gets here
        return self.humanName

    def setHumanName(self, humanName):
        #user validation gets here
        self.humanName = humanName
    
    def getHumanHeight(self):
        #user validation gets here
        return self.humanHeight

    def setHumanHeight(self, humanHeight):
        #user validation gets here
        self.humanHeight = humanHeight
    
    def getHumanIq(self):
        #user validation gets here
        return self.humanIq

    def setHumanIq(self, humanIq):
        #user validation gets here
        self.humanIq = humanIq
        
    def displayHuman(self):
        print("{} is {} and has an iq of {}.".format(self.getHumanName(), self.getHumanHeight(), self.getHumanIq()))