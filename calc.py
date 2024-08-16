"""
Justin Choi
IDT Period 3
4 January 2023
Calculations
"""

import math
import random
import decimal

#defines main
def main():
    
    #Integer calculation
    f = 0
    y = random.randint(1, 100)
    while(f == 1):
        
        x = int(input("Pick a number 1 - 100: "))
        
        if(x < y):
            print("Too low!")
        if(x > y):
            print("Too high!")
        if(x == y): 
            print("Good job!")
            f = 1
    #Float
    y = random.randint(1, 1000)
    x = int(input("Guess a number: "))
    z = 0
    b = 0
    t = 0
    n = y
    while(t == 0):

        print(y)
        z = n / 2
        print(z)
        c = int(z)
        print(c)
        b += 1
        n = z
        print(str(y) + " Has been divided " + str(b) + " time(s)")
        
        if(float(c) == z):
            t = 0
        if(float(c) != z):
            t = 1
    if(x == b):
        print("Good job you win!")
    if(x != b):
        print("Close one!")
    #decimal
    
    print("multiplying decimals")
    #Gets a decimal value
    x = decimal.Decimal(input("Enter the first number: "))
    y = decimal.Decimal(input("Enter the second number: "))
    
    #caps the amount of digits
    decimal.getcontext().prec = 10
    z = x * y
    print("The product is: " + str(z))
    
    
    #byte
    x = "Coding is super fun!"
    y = bytes(x, "utf-8")
    print(x)
    print(y)
    x = 15
    y = bytes(x)
    print(x)
    print(y)
     
#calls main
if(__name__ == "__main__"):
    main()