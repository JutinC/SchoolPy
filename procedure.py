"""
Justin Choi
IDT Period 3
5 January 2023
Procedures
"""
import math
import random
import time

#creates a procedure for a list outside of main
def list1(cow):

    list = ["Cat", "Sheep", "Pig", "Dog", "Cow"]
    list.insert(3, cow)
    print(list)

#creates a procedure to calculate area of a triangle
def calculator(x):
    
    y = x ** 2 * math.pi
    z = x ** 2
    print(str(y) + " or " + str(z) + "pi")
    
#create a procedure to a
def coin(x):
    y = random.randint(1, 2)
    print("Flipping coin...")
    time.sleep(1)
    if(x == "Heads"):
        if(y == 1):
            print("Heads. Good job!")
        if(y == 2):
            print("Tails. Nice try!")
    if(x == "Tails"):
        if(y == 1):
            print("Heads. Nice try!")
        if(y == 2):
            print("Tails. Good job!")

def main():
    
    
    list = ["Cat", "Sheep", "Pig", "Dog", "Cow"]
    print(list)
    x = str(input("Enter an animal not on the list: "))
    #Calls the procedure outside of main to add an item on the list
    list1(x)
    
    print("Calculating the area of a circle")
    x = float(input("Enter the radius: "))
    #Calls the procedure to solve the equation
    
    calculator(x)
    print("Coinflip")
    x = str(input("Heads or Tails: "))
    #Calls the procedure to flip the coin and check if right
    coin(x)
    
    
    

    
    

if(__name__ == "__main__"):
    main()