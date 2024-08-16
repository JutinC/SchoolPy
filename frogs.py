"""
Justin Choi
IDT Period 3
6 January 2023
Princess Class
"""

import os, sys
from princess import Princess

def main():
    
    #Creating a Princess
    princessOfTheDay = Princess("Cinderella", 5) #object
    
    #Display the princess' state
    princessOfTheDay.displayPrincess()

    #Mutating the fields
    princessOfTheDay.setPrincessName("Ariel")
    princessOfTheDay.displayPrincess()
    princessOfTheDay.setNumFrogs(30)
    princessOfTheDay.displayPrincess()

    sally = Princess("sally", 13)
    sally.displayPrincess()
    
if(__name__ == "__main__"):
    main()