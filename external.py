"""
Justin Choiexit
IDT Period 3
6 January 2023
External Libraries
"""
#external libraries
import math #1
import random #2
from fractions import Fraction #3

def main():
    #uses the fraction external library
    x = str(input("What is the probability that someone wins given they chose rock: "))
    if(Fraction(x) == Fraction("1/3")):
        print("Good Job")
    if(Fraction(x) != Fraction("1/3")):
        print("Incorrect")
    #uses the random external library
    z = random.randint(1, 3)
    y = str(input("Rock Paper Scissors: "))
    print("You chose " + y)
    
    if(y == "Rock"):      
        if(z == 1):
            print("I chose Rock")
            print("Tie")
        if(z == 2):
            print("I chose Scissors")
            print("You win")
        if(z == 3):
            print("I chose Paper")
            print("You lose")
             
    if(y == "Paper"):      
        if(z == 1):
            print("I chose Rock")
            print("You win")
        if(z == 2):
            print("I chose Scissors")
            print("You lose")
        if(z == 3):
            print("I chose Paper")
            print("Tie")
    
    if(y == "Scissors"):      
        if(z == 1):
            print("I chose Rock")
            print("You lose")
        if(z == 2):
            print("I chose Scissors")
            print("tie")
        if(z == 3):
            print("I chose Paper")
            print("You win")
    print("Circumference calculator")
    x = float(input("Enter the radius: "))
    #uses the math external library
    y = x * 2 * math.pi
    print("The circumference is: " + str(y))
        
    
    # x = int(input())

if(__name__ == "__main__"):
    main()


