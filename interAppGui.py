"""
Justin Choi
Period 3
IDT
Febuary 1
interactive
"""

import tkinter as tk

class Interactive():
    
    def __init__(self):
        #Creates canvas
        mainWin = tk.Tk()
        
        #Sets the title of the window
        mainWin.title("Interaction")
        
        #Sets the row and column 
        mainWin.rowconfigure(0, minsize = 1, weight = 1)
        mainWin.rowconfigure(1, minsize = 500, weight = 1)
        mainWin.columnconfigure(1, minsize = 10, weight = 1)
        mainWin.columnconfigure(2, minsize = 600, weight = 1)
      
        #Creates an interactive text
        entry = tk.Entry(mainWin, bd = 5)
        lbl = tk.Label(mainWin, text = "In")
        btn_Frame = tk.Frame(mainWin, relief = tk.RAISED)
        
        #initializes a label to later insert
        lbl2 = tk.Label(mainWin, text = "I like Potatoes", font = 'Helvetica 13')

        #Creates a button
        btn = tk.Button(btn_Frame, text = 'Read', bd = 5, command = lambda: self.readData(entry, lbl2))
        btn2 = tk.Button(btn_Frame, text = 'Write', bd = 5, command = lambda: self.writeData(entry, "I like potatoes"))
        
        #Positions the button, label, and entry 
        btn.grid(row = 0, column = 0, sticky = 'ew')
        btn2.grid(row = 1, column = 0, sticky = 'ew')
        btn_Frame.grid(row = 0, column = 0, sticky = 'ns')
        lbl.grid(row = 0, column = 1, sticky = 'nw')
        entry.grid(row = 0, column = 2, sticky = 'nw')
        lbl2.grid(row = 1, column = 2, sticky = 'ew')
        
        #packs to display the stuff
        mainWin.mainloop()
        
    def readData(self, entry, lbl):
        lbl.config(text = entry.get())

    def writeData(self, entry, text):
        entry.delete(0, tk.END)
        entry.insert(0, text)
        