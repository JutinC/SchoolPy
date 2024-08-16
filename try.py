"""
Justin Choi
IDT Period 3
12 January 2023
try except
"""

def main():
    #tries
    check = 0
    while(check == 0):  
        x = str(input("choose int or string: "))
        
        if(x == "int"):
            y = int(input("Pick any number: "))
            check = 1
            
        if(x == "string"):
            y = str(input("Write anything: "))
            check = 1
    try:
        print(int(y))
        try:
            z = y + y
            print("Printing " + str(y) + " + " + str(y))
            print(str(y) + " + " + str(y) + " = " + z)
        except:
            print("Error: Cannot combine string with integer")
    except:
        print("Not an integer")
        print(str(y))
    finally:
        print(str(y) + " has been printed")

    

if (__name__ == "__main__"):
    main()