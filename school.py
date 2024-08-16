"""
Justin Choi
IDT Period 3
12 January 2023
Container
"""
from human import Human
class School():
    
    def __init__(self):  #initiates class
        self.schoolTrans =  []
        self.schoolTrans.append(Human("Justin", "5'8", 170))
       
    #Getter
    def getSchoolTrans(self):
        #user validation gets here
        return self.schoolTrans
    #Setter
    def setSchoolTrans(self, schoolTrans):
        #user validation gets here
        self.schoolTrans = schoolTrans
        
    
    def addStudent(self, student: Human):
        #CREATES a student to the list
        self.schoolTrans.append(student)
    
    def displayStudents(self):
        #READS everything in the list
        print("Students enrolled in JCHS")
        for i in self.schoolTrans:
            i.displayHuman()

    #Sets the value
    def failTest(self,student: Human):
        #UPDATES the Human IQ
        student.humanIq *= 0.5
        print(student.humanName + " has failed a test. Iq lowered")
        
    def removeStudent(self, student: Human):
        print("{}, with an iq of {}, was suspended".format(student.humanName,student.humanIq))
        #DELETES the student
        self.schoolTrans.remove(student)
    
    def numStudents(self): 
        #Defines the amount of students in the list into a variable
        num = len(self.schoolTrans)
        #Proper grammar
        if(len(self.schoolTrans) == 1):
            print("There is {} student.".format(num))
        if(len(self.schoolTrans) != 1):
            print("There are {} students.".format(num))
    
        

