"""
Justin Choi
IDT Period 3
12 January 2023
Container
"""


import os, sys
import time
#Imports the original poco
from human import Human
#Imports the container
from school import School

def main():
    
    #Defines a Human
    saatvik = Human("Saatvik", "5'5", 10)
    Linbo = Human("Linbo", "Scammer", 170)
    Hayden = Human("Hayden", "average", 999)
    Alex = Human("Alex", "short", 101)
    school = School()
    

    #Creates a student in the list
    school.addStudent(saatvik)
    school.addStudent(Linbo)
    school.addStudent(Hayden)
    
    #Reads the students
    school.displayStudents()
    
    #Prints the number of students enrolled
    school.numStudents()
    
    #Deletes a student
    school.removeStudent(saatvik)
    
    #Reads the students
    school.displayStudents()
    #Prints the number of students enrolled
    school.numStudents()
    
    #Updates a student
    school.failTest(Linbo)
    
    #Reads the students
    school.displayStudents()
    #Prints the number of students enrolled
    school.numStudents()
    
    
if __name__ == "__main__":
    main()