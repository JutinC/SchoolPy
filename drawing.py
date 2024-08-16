"""
Rudolph
"""

import tkinter as tk
import random

def rgbtrans(rgb):
    return "#%02x%02x%02x" % rgb

def main():

    #Create a main window
    mainWin = tk.Tk()

    #Create a canvas on which to draw
    canvas = tk.Canvas(mainWin, bg= rgbtrans((46, 171, 255)), height = 750, width = 1000)

    #Creates the snowy floor
    snow = canvas.create_rectangle(1020, 775, 0, 500, fill = "white")

    #Makes snow bits appear everywhere without coding each little thing
    r = 0
    while r < 500:
        x = random.randint(1, 1000)
        y = random.randint(1, 500)
        snow = canvas.create_oval(x, y, x, y, fill = "white")
        r += 1

    #Creates a tree
    trunk = canvas.create_rectangle(600, 300, 650, 500, fill = rgbtrans((139, 69, 19)), outline = rgbtrans((139, 69, 19)))
    leaf1 = canvas.create_polygon(440,450,625,200,810,450, fill="green")
    leaf2 = canvas.create_polygon(450,350,625,150,800,350, fill="green")
    leaf3 = canvas.create_polygon(460,250,625,100,790,250, fill="green")
    
    #Creates ornaments
    l = 0
    while l < 30:
        i = random.randint(500, 700)
        o = random.randint(150, 425)
        u = i + 10
        p = o + 10
        orb = canvas.create_oval(i, o, u, p, fill = "red", outline = "red")
        l += 1
        
    #Makes legs
    leg1 = canvas.create_oval(275, 425, 325, 500, fill = rgbtrans((150, 75, 25)), outline = "black")
    leg2 = canvas.create_oval(175, 425, 125, 500, fill = rgbtrans((150, 75, 25)), outline = "black")
    arm1 = canvas.create_oval(150, 340, 100, 410, fill = rgbtrans((150, 75, 25)), outline = "black")
    arm2 = canvas.create_oval(300, 340, 350, 410, fill = rgbtrans((150, 75, 25)), outline = "black")
   
    #Makes the body 
    body1 = canvas.create_oval(315, 280, 135, 475, fill = rgbtrans((150, 75, 25)), outline = "black")
    
    #Makes ears as oval and first so it doesnt overlap the head
    ear1 = canvas.create_oval(25, 100, 150, 150, fill = rgbtrans((150, 75, 25)), outline = "black")
    e1 = canvas.create_oval(50, 110, 130, 140, fill = rgbtrans((200, 150, 100)), outline = "black")
    ear2 = canvas.create_oval(425, 100, 300, 150, fill = rgbtrans((150, 75, 25)), outline = "black")
    e2 = canvas.create_oval(405, 110, 315, 140, fill = rgbtrans((200, 150, 100)), outline = "black")

    #horns next to appear in from of ears but still connected to head
    horn1 = canvas.create_line(130, 80, 150, 150, fill = "black", width = 30)
    horn2 = canvas.create_line(325, 80, 300, 150, fill = "black", width = 30)

    #Main head for face
    head = canvas.create_oval(100, 100, 350, 300, fill = rgbtrans((150, 75, 25)), outline = rgbtrans((100, 70, 50)))
    head2 = canvas.create_oval(150, 300, 300, 200, fill = rgbtrans((200, 150, 100)), outline = "black")

    #nose
    nose = canvas.create_oval(200, 200, 250, 250, fill = "red", outline = "red")

    #Eye and pupils on top
    eye1 = canvas.create_oval(150, 150, 200, 230, fill = "white", outline = "black")
    i1 = canvas.create_oval(150, 170, 198, 225, fill = "black", outline = "black")
    eye2 = canvas.create_oval(250, 150, 300, 230, fill = "white", outline = "black")
    i2 = canvas.create_oval(250, 170, 298, 225, fill = "black", outline = "black")

    #Mouth since order does not matter from nose and eyes and top part
    mouth = canvas.create_arc(275, 250, 175, 280, start = 180, extent = 180, fill = "black", outline = "black")
    tongue = canvas.create_arc(250, 260, 200, 280, start = 180, extent = 180, fill = "red", outline = "red")

    canvas.pack()
    mainWin.mainloop()


if(__name__=="__main__"):
    main()