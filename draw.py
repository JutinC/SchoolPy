"""
Header
"""

import tkinter as tk

def main():

    #Create a main window
    mainWin = tk.Tk()

    # #Create image

    # img1 = tk.PhotoImage(file="file.png")
    # canvas.create_image(200, 300, image = img1)
    
    #Create a canvas on which to draw
    canvas = tk.Canvas(mainWin, bg= "white", height = 750, width = 835)

    #Create coordinates
    coord = 300,50,100,210

    #Draw an arc with the coordinates
    arc = canvas.create_arc(coord, start = 0, extent = 150, fill = "red")

    #draw a line
    line1 = canvas.create_line(0, 0, 100, 100, fill = "orange", width = 10)

    #Draw a circle
    circle1 = canvas.create_oval(200, 200, 300, 300, fill = "purple")

    #Draw a Rectangle
    rectange1 = canvas.create_rectangle(100, 400, 150, 450, fill = "black")

    canvas.pack()
    mainWin.mainloop()


if(__name__=="__main__"):
    main()