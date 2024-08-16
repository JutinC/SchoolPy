"""
Justin Choi
IDT Period 3
11 January 2023
Dogs Class
"""

import os, sys
from dog import Dogs

def main():
    
    #Creating a Dog 1
    dog = Dogs("Fluffy", "Bichon", 2)
    #Creating a Dog 2
    hayden = Dogs("Hayden", "Human", 15)
    #Creating a Dog 3
    alex = Dogs("Alex", "Labradout", 4)  
      
    #Display the Dog's state 1
    dog.displayDog()
    #Display the Dog's state 2
    hayden.displayDog()
    #Display the Dog's state 3
    alex.displayDog()
    


    
if __name__ == "__main__":
    main()