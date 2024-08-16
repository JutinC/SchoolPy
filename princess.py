""""
Justin Choi
IDT Period 3
6 January 2023
Princess Class
"""

#class is a recipe for an object, custom data type, map of memory
class Princess():
    
    #Constructor for the Princess Class
    def __init__(self, princessName, numFrogs): #signature
        self.princessName = princessName
        self.numFrogs = numFrogs
        
    #Getters and Setters Section
    #Getters are also called ACCESSORS
    #Setters are called MUTATORS
    
    def getPrincessName(self):
        #user validation gets here ALWAYS DO THIS COMMENT
        return self.princessName

    def setPrincessName(self, princessName):
        #user validation gets here
        self.princessName = princessName
    
    def getNumFrogs(self):
        #user validation gets here
        return self.numFrogs

    def setNumFrogs(self, numFrogs):
        #user validation gets here
        self.numFrogs = numFrogs
        
    def displayPrincess(self):
        print("Princess Report")
        print("Princess {} has kissed {} frogs.".format(self.getPrincessName(), self.getNumFrogs()))