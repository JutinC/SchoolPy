"""
Justin Choi
IDT Period 3
4 January 2023
Hello World
"""

#defines main
def main():
    
    
    y = 0 # sets variable value

    while(y < 1): # repeats input unless wanted otherwise
        
        x = str(input("\033[037m" + "Insert a primary color: ")) # gets user input as a string
        
        #list of options depending on option 
        if(x == "red"):
            print("\033[0;91m" + "Hello, world!" + "\033[037m")
            
        if(x == "blue"):
            print("\033[0;94m" + "Hello, world!" + "\033[037m")
        #primary color of light    
        if(x == "green"):
            print("\033[0;92m" + "Hello, world!" + "\033[037m")
        #primary color of pigment    
        if(x == "yellow"):
            print("\033[0;93m" + "Hello, world!" + "\033[037m")

        if(x == "stop"): #stops program whenever
            y = 1
        
    
#calls main
if(__name__ == "__main__"):
    main()