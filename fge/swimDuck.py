""""
Justin Choi
3 Period
9 May 2023
IDT 
Swim Game (I am Swimming for summer)
"""
import tkinter as tk, PIL.Image, PIL.ImageTk

class Duck:
    
    def __init__(self):
        #Set the variables
        self.x, self.y = 0, 0
        #Set the main Window
        self.mainWin = tk.Tk()
        #Create the geometry space
        self.mainWin.geometry('500x800')
        #Create a loop
        self.running = True
        #Converting image of duck player 
        self.duckImage=PIL.ImageTk.PhotoImage(PIL.Image.open("/Users/imatable/SchoolPy/fge/swimDuck.png").convert("RGBA").resize((100,100)))
        #Title
        self.mainWin.title("Duckyswim")
        #Creating canvas
        self.canvas = tk.Canvas(width=500, height=800, bg='blue')
        self.canvas.place(x=0, y=0)
        
        #To make the game keep running
        while self.running:
                #Calling procedure to change x and y value
                self.mainWin.bind('<KeyPress>', self.press)
                #Calling the function
                self.duckX, self.duckY = self.findDuckX(), self.findDuckY()
                #Covers the old duck to show new duck position
                self.canvas.create_rectangle(0,0,500,800, fill='blue', outline=None)
                #Place duck pack on canvas
                self.canvas.create_image(self.duckX,self.duckY,anchor='nw',image=self.duckImage)
                try:
                    #Update to see changes
                    self.mainWin.update()
                except:
                    #Stops loop from bieng infinite
                    self.running=False
            
    #Procedure to change position when certain key is pressed
    def press(self, event):
        #Find which key is pressed then change position based on that
        if(event.keysym == "w"):
            self.y -=5
        if(event.keysym == "a"):
            self.x -=5
        if(event.keysym == "s"):
            self.y +=5
        if(event.keysym == "d"):
            self.x +=5
        
    #Functions to find x and y position
    def findDuckX(self):
        return 200 + self.x
    
    def findDuckY(self):
        return 600 + self.y
        
        
        
def main():
    duck = Duck()
    
if(__name__ == "__main__"):
    main()