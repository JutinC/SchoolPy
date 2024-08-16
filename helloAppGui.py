"""
Justin Choi
Period 3
IDT
Febuary 1
Hello World as Poco
"""

import tkinter
import random

class Hello:
    
    def __init__(self):
        
        #Creates canvas
        mainWin = tkinter.Tk()
        
        #Sets the geometry
        mainWin.geometry('1000x1000')
        
        #Create object for canvas
        canvas = tkinter.Canvas(mainWin, bg = 'white', height = 1000, width = 1000)
        
        #Creates a little rectangle
        helloWorld = canvas.create_rectangle(0, 0, 1000, 1000, fill = "red", outline = 'black')
        #Adds text of hello world
        text = canvas.create_text(500, 300, text = "Hello, World!", font = ('Times New Roman', '100', 'bold'))
        #packs to display the stuff
        canvas.pack()
        mainWin.mainloop()