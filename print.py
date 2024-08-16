"""
Justin Choi
IDT Period 3
4 January 2023
Print
"""

#defines main
def main():
    #sets a variable
    x = 4
    y = 6
    
    #does python inputed math
    z = int(x) + int(y)
    
    #sets a list
    list = ["Math", "Band", "IDT", "Lunch", "Bio", "Gov", "Lit"]

    #makes another problem
    u = 1 + 420 / z
    
    #print with a variable
    print(str(x) + " + " + str(y) + " = " + str(z))

    #print the list first all the way to one before the fourth
    print(list)
    print(list[0:3])
    print(list [5:7])
    
    #print a placeholder
    print("There are {} Cats.".format("42"))
    print(f"There are {x} Dogs.")
    
    #print a float
    print("There are {} Potatoes.".format(float(u)))
    
    #print normally
    print("A box is 12 lbs.")
    
#calls main
if(__name__ == "__main__"):
    main()


#tabulators
#ibm 
# a class is a recipe for an object
# a class is a memory map
# class into memory and becomes object
# Ex. x = 4
#class have attributes or fields of class
#constructor