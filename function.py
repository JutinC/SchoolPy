"""
Justin Choi
IDT Period 3
5 January 2023
Procedures
"""

import random
import time
#function to check if works
def check(x):
    if(x != "left" and x != "right" and x != "middle"):
        return 0
    if(x == "left" or x == "right" or x == "middle"):
        return 1

#function to calculate ai move
def ai():
    p = random.randint(1, 3)
    if(p == 1):
        return "left"
    if(p == 2):
        return "right"
    if(p == 3):
        return "middle"

#function to calculate the standoff
def standoff(hide, shoot):
    if(hide == shoot):
        return 1
    if(hide != shoot):
        return 0
        
    
def main():
    
    restart = 0
    aiScore = 0
    pScore = 0
    print("GamePigeon Paintball")
    print("Options are left, right, middle")
    while(restart == 0):
        c = 0
        while(c == 0):
            pHide = str(input("Where to hide: "))
            #calls a function to check if right
            c = check(pHide)
        c = 0
        while(c == 0):
            pShoot = str(input("Where to shoot: "))
            #calls same function
            c = check(pShoot)
        #calls function to find the ai move
        aiHide = ai()
        aiShoot = ai()
        #aiHide vs pShoot
        print("You shot at the " + pShoot)
        time.sleep(1)
        print("Ai hid at the " + aiHide)
        
        #Calls function to calculate the result
        aiLife = standoff(aiHide, pShoot)
        if(aiLife == 1):
            print("You paintballed him!")
            pScore += 1
        if(aiLife == 0):
            print("You missed!")
        time.sleep(2)
        
        print("__________________")
        print("You hid at the " + pHide)
        time.sleep(1)
        print("Ai shot at the " + aiShoot)
        
        #Calls function to calculate the result
        pLife = standoff(pHide, aiShoot)
        if(pLife == 1):
            print("You got paintballed!")
            aiScore += 1
        if(pLife == 0):
            print("Ai missed!")
        time.sleep(2)
        print("Ai: " + str(aiScore))
        print("You: " + str(pScore))  
        print("(yes or no)")
        reCheck = str(input("Play again? "))  
        if(reCheck == "yes"):
            pass
        if(reCheck == "no"):
            restart = 1
    
    
    
    
    
    

    

if(__name__ == "__main__"):
    main()